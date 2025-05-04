from telethon import events
from telethon.tl.functions.contacts import BlockRequest
import pickle
import asyncio
import os

afk_mode = False
custom_reply = "أنا لست موجودًا الآن، أرجوك اترك رسالتك وانتظر لحين عودتي."
allowed_chats = set()
warning_counts = {}
max_warnings = 3
developer_id = 5434703779 

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.تشغيل الرد$'))
async def xyz1(event):
    global afk_mode
    afk_mode = True
    await event.edit("**⌯ تـم تشغيل الرد التلقائي.**", parse_mode="md")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.تعطيل الرد$'))
async def xyz2(event):
    global afk_mode
    afk_mode = False
    await event.edit("**⌯ تـم تعطيل الرد التلقائي.**", parse_mode="md")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.تعيين كليشة الرد$'))
async def xyz3(event):
    reply_template = await event.get_reply_message()
    if reply_template:
        with open('reply_template.pickle', 'wb') as f:
            pickle.dump(reply_template.text, f)
        await event.edit("**⌯ تـم تعيين كليشة الرد إلى الرسالة المحددة.**", parse_mode="md")
    else:
        await event.edit("**⌯ يرجى الرد على الرسالة التي تريد استخدامها ككليشة.**", parse_mode="md")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.تعيين صورة الرد$'))
async def xyz4(event):
    reply_to = await event.get_reply_message()
    if reply_to and reply_to.media:
        try:
            file_path = await event.client.download_media(reply_to.media)
            with open('reply_image.pickle', 'wb') as f:
                pickle.dump(file_path, f)
            await event.edit("**⌯ تـم تعيين صورة الرد إلى الصورة المحددة.**", parse_mode="md")
        except Exception as e:
            await event.edit(f"**⌯ حدث خطأ أثناء حفظ الصورة: {e}**", parse_mode="md")
    else:
        await event.edit("**⌯ يرجى الرد على صورة/فيديو/GIF لتعيينها كصورة رد.**", parse_mode="md")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.تعيين كليشة الحظر$'))
async def xyz5(event):
    block_template = await event.get_reply_message()
    if block_template:
        with open('block_template.pickle', 'wb') as f:
            pickle.dump(block_template.text, f)
        await event.edit("**⌯ تـم تعيين كليشة الحظر إلى الرسالة المحددة.**", parse_mode="md")
    else:
        await event.edit("**⌯ يرجى الرد على الرسالة التي تريد استخدامها ككليشة حظر.**", parse_mode="md")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.تعيين صورة الحظر$'))
async def xyz6(event):
    reply_to = await event.get_reply_message()
    if reply_to and reply_to.media:
        try:
            file_path = await event.client.download_media(reply_to.media)
            with open('block_image.pickle', 'wb') as f:
                pickle.dump(file_path, f)
            await event.edit("**⌯ تـم تعيين صورة الحظر إلى الصورة المحددة.**", parse_mode="md")
        except Exception as e:
            await event.edit(f"**⌯ حدث خطأ أثناء حفظ الصورة: {e}**", parse_mode="md")
    else:
        await event.edit("**⌯ يرجى الرد على صورة/فيديو/GIF لتعيينها كصورة حظر.**", parse_mode="md")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.التحذيرات (\d+)$'))
async def xyz7(event):
    global max_warnings
    try:
        max_warnings = int(event.pattern_match.group(1))
        await event.edit(f"**⌯ تـم تعيين عدد التحذيرات إلى {max_warnings}.**", parse_mode="md")
    except ValueError:
        await event.edit("**⌯ يرجى إدخال رقم صحيح لعدد التحذيرات.**", parse_mode="md")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.سماح$'))
async def xyz8(event):
    if event.is_private:
        allowed_chats.add(event.chat_id)
        async for message in event.client.iter_messages(event.chat_id, from_user=event.sender_id):
            if "تبقى لديك" in message.text:
                await message.delete()
        await event.edit("**⌯ تـم السماح لهذه المحادثة.**", parse_mode="md")
    else:
        await event.edit("**⌯ لا يمكن استخدام هذا الأمر إلا في المحادثات الخاصة.**", parse_mode="md")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.رفض$'))
async def xyz9(event):
    if event.is_private:
        allowed_chats.discard(event.chat_id)
        await event.edit("**⌯ تـم إلغاء السماح لهذه المحادثة.**", parse_mode="md")
    else:
        await event.edit("**⌯ لا يمكن استخدام هذا الأمر إلا في المحادثات الخاصة.**", parse_mode="md")
    await asyncio.sleep(2)
    await event.delete()

@events.register(events.NewMessage)
async def xyz10(event):
    global warning_counts, max_warnings, afk_mode

    if not afk_mode or not event.is_private or event.chat_id in allowed_chats or event.sender_id == developer_id:
        return

    me = await event.client.get_me()
    sender = await event.get_sender()
    if sender.id == me.id or sender.bot:
        return

    reply_template = None
    if os.path.exists('reply_template.pickle'):
        with open('reply_template.pickle', 'rb') as f:
            reply_template = pickle.load(f)

    block_template = None
    if os.path.exists('block_template.pickle'):
        with open('block_template.pickle', 'rb') as f:
            block_template = pickle.load(f)

    user_id = sender.id

    if reply_template and ("{warns}" in reply_template and "{totalwarns}" in reply_template):
        warning_counts[user_id] = warning_counts.get(user_id, 0) + 1
        warns = warning_counts[user_id]
        remaining = max_warnings - warns
        formatted_reply = reply_template.format(
            mention=f"[{sender.first_name}](tg://user?id={sender.id})",
            warns=warns,
            totalwarns=max_warnings
        )

        if warns >= max_warnings:
            formatted_block = block_template or "لقد تم حظرك لتجاوز الحد المسموح من الرسائل."
            if "{mention}" in formatted_block:
                formatted_block = formatted_block.format(
                    mention=f"[{sender.first_name}](tg://user?id={sender.id})"
                )

            if os.path.exists('block_image.pickle'):
                with open('block_image.pickle', 'rb') as f:
                    file_path = pickle.load(f)
                await event.client.send_file(event.chat_id, file_path, caption=formatted_block)
            else:
                await event.reply(formatted_block)

            await event.client(BlockRequest(user_id))
            del warning_counts[user_id]
        else:
            if os.path.exists('reply_image.pickle'):
                with open('reply_image.pickle', 'rb') as f:
                    file_path = pickle.load(f)
                await event.client.send_file(event.chat_id, file_path, caption=formatted_reply)
            else:
                await event.reply(formatted_reply)

    elif warning_counts.get(user_id, 0) == 0:
        warning_counts[user_id] = 1
        if reply_template:
            reply_text = reply_template.format(
                mention=f"[{sender.first_name}](tg://user?id={sender.id})"
            )
        else:
            reply_text = custom_reply
        await event.reply(reply_text)
