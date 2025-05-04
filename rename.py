import asyncio
import random
from telethon import events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import pytz
import FINAL

client = FINAL.client.client
update_tasks = {}

time_formats = {
    "1": "𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎",
    "2": "𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶",
    "3": "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢",
    "4": "𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬",
    "5": "𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶",
    "6": "۱۲۳۴۵۶۷۸۹۰",
    "7": "١٢٣٤٥٦٧٨٩٠",
    "8": "₁₂₃₄₅₆₇₈₉₀",
    "9": "⓵⓶⓷⓸⓹⓺⓻⓼⓽⓪",
    "10": "①②③④⑤⑥⑦⑧⑨⓪",
    "11": "𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘",
    "12": "❶❷❸❹❺❻❼❽❾⓿"
}

current_time_format = "1"

arabic_timezones = {
    "الإمارات": "Asia/Dubai",
    "البحرين": "Asia/Bahrain",
    "الجزائر": "Africa/Algiers",
    "جيبوتي": "Africa/Djibouti",
    "السعودية": "Asia/Riyadh",
    "السودان": "Africa/Khartoum",
    "الصومال": "Africa/Mogadishu",
    "العراق": "Asia/Baghdad",
    "عمان": "Asia/Muscat",
    "فلسطين": "Asia/Gaza",
    "قطر": "Asia/Qatar",
    "جزر القمر": "Indian/Comoro",
    "الكويت": "Asia/Kuwait",
    "لبنان": "Asia/Beirut",
    "ليبيا": "Africa/Tripoli",
    "مصر": "Africa/Cairo",
    "المغرب": "Africa/Casablanca",
    "موريتانيا": "Africa/Nouakchott",
    "اليمن": "Asia/Aden",
    "تونس": "Africa/Tunis",
    "الأردن": "Asia/Amman",
    "سوريا": "Asia/Damascus"
}

def format_time(time_obj):
    formatted_time = time_obj.strftime('%I:%M')
    original_chars = "1234567890"
    formatted_chars = time_formats[current_time_format]
    for i in range(len(original_chars)):
        formatted_time = formatted_time.replace(original_chars[i], formatted_chars[i])
    return formatted_time

async def update_name_periodically(event, user_name, timezone_str):
    chat_id = event.chat_id
    timezone = pytz.timezone(timezone_str)
    await event.delete()

    while update_tasks.get(chat_id, {}).get("name", False):
        now = datetime.now(timezone)
        formatted_time = format_time(now)

        try:
            await event.client(UpdateProfileRequest(last_name=formatted_time))
        except Exception as ex:
            print(f"حدث خطأ: {str(ex)}")

        await asyncio.sleep(60 - now.second)

async def update_bio_periodically(event, timezone_str, bios=None):
    chat_id = event.chat_id
    timezone = pytz.timezone(timezone_str)
    await event.delete()

    while update_tasks.get(chat_id, {}).get("bio", False):
        now = datetime.now(timezone)
        formatted_time = format_time(now)

        if bios:
            chosen_bio = random.choice(bios)
            final_bio = f"{chosen_bio} | {formatted_time}"
        else:
            final_bio = f"⌯ {formatted_time}"

        try:
            await event.client(UpdateProfileRequest(about=final_bio))
        except Exception as ex:
            print(f"خطأ في تحديث البايو: {str(ex)}")

        await asyncio.sleep(60 - now.second)

@events.register(events.NewMessage(pattern=r".اسم_وقتي (.+)", outgoing=True))
async def change_name_with_time(event):
    country = event.pattern_match.group(1)
    if country in arabic_timezones:
        timezone_str = arabic_timezones[country]
        chat_id = event.chat_id

        if chat_id not in update_tasks:
            update_tasks[chat_id] = {}

        update_tasks[chat_id]["name"] = True
        me = await client.get_me()
        user_name = me.first_name
        asyncio.ensure_future(update_name_periodically(event, user_name, timezone_str))
    else:
        await event.respond("** ⌯ الـبلد غـير موجـود فـي القائمـة.**", parse_mode="md")

@events.register(events.NewMessage(pattern=r".بايو_وقتي (.+)", outgoing=True))
async def change_bio_with_time(event):
    country = event.pattern_match.group(1)
    if country not in arabic_timezones:
        await event.respond("** ⌯ البلد غير موجود في القائمة.**", parse_mode="md")
        return

    timezone_str = arabic_timezones[country]
    chat_id = event.chat_id

    if chat_id not in update_tasks:
        update_tasks[chat_id] = {}

    update_tasks[chat_id]["bio"] = True

    bios = None
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        if reply_msg.text:
            bios = [line.strip() for line in reply_msg.text.splitlines() if line.strip()]

    asyncio.ensure_future(update_bio_periodically(event, timezone_str, bios))

@events.register(events.NewMessage(pattern=r".ايقاف الاسم$", outgoing=True))
async def stop_name_update(event):
    chat_id = event.chat_id
    if chat_id not in update_tasks:
        update_tasks[chat_id] = {}
    update_tasks[chat_id]["name"] = False
    try:
        await event.client(UpdateProfileRequest(last_name=""))
        await event.respond("** ⌯ تـم إيقاف الاسم الوقتي قسرياً.**", parse_mode="md")
    except Exception as ex:
        await event.respond(f"** ⌯ حدث خطأ أثناء إيقاف الاسم: {str(ex)}**", parse_mode="md")
    await event.delete()

@events.register(events.NewMessage(pattern=r".ايقاف البايو$", outgoing=True))
async def stop_bio_update(event):
    chat_id = event.chat_id
    if chat_id not in update_tasks:
        update_tasks[chat_id] = {}
    update_tasks[chat_id]["bio"] = False
    try:
        await event.client(UpdateProfileRequest(about=""))
        await event.respond("** ⌯ تـم إيقاف البايو الوقتي قسرياً.**", parse_mode="md")
    except Exception as ex:
        await event.respond(f"** ⌯ حدث خطأ أثناء إيقاف البايو: {str(ex)}**", parse_mode="md")
    await event.delete()

@events.register(events.NewMessage(pattern=r"\.اشكال الوقت$", outgoing=True))
async def show_time_formats(event):
    formats_text = "\n".join([f"{key}: {value}" for key, value in time_formats.items()])
    await event.respond(f"** ⌯ قائمـة أشكـال الوقـت:**\n\n{formats_text}", parse_mode="md")
    await event.delete()

@events.register(events.NewMessage(pattern=r"\.الشكل (\d+)", outgoing=True))
async def change_time_format(event):
    global current_time_format
    format_key = event.pattern_match.group(1)
    if format_key in time_formats:
        current_time_format = format_key
        await event.respond(f"** ⌯ تـم تغيـير شكـل الوقـت إلـى {format_key}**", parse_mode="md")
    else:
        await event.respond("** ⌯ شكـل الوقـت غـير موجـود.**", parse_mode="md")
    await event.delete()