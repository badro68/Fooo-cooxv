from telethon import events
import time
import FINAL.client
client = FINAL.client.client


ketdi = ["░░░░░░🚜░░░░░░🏠\n█████████████████",
 "░░░░░░🚜░░░░░🚶🏠\n█████████████████",
 "░░░░░░🚜░░░░🚶░🏠 \n█████████████████",
 "░░░░░░🚜░░🚶░░░🏠 \n█████████████████",
 "░░░░░░🚜🚶░░░░░🏠 \n█████████████████",
 "░░░░░░🚜░░░░🇰░🏠 \n█████████████████",
 "░░░░░🚜░░░░░░░░🏠 \n█████████████████",
 "░░░░🚜░░░🇰 🇪 ░🏠\n█████████████████",
 "░░░🚜░🇰 🇪 🇹░░🏠\n█████████████████",
 "░🚜░🇰 🇪 🇹 🇩 🏠\n█████████████████",
 "🚜░🇰 🇪 🇹 🇩 🇮🏠\n █████████████████",
 "🇰 🇪 🇹 🇩 🇮 🇲🏠\n█████████████████"]
@events.register(events.NewMessage)
async def ketdihandlers(event):
		if event.raw_text == '.ذهبت':  
			time.sleep(0.3)
			for d in ketdi:
				time.sleep(0.3)
				await event.edit(d)
