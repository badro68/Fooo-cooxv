import asyncio
from telethon import events 
import time
import random
import FINAL.client
client = FINAL.client.client

M = ("___________ \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　／￣￣＼| \n"
"＜ ´･ 　　 |＼ \n"
"　|　３　 | 丶＼ \n"
"＜ 、･　　|　　＼ \n"
"　＼＿＿／∪ _ ∪) \n"
"　　　　　 Ｕ Ｕ\n")
    
C = ("_/﹋\_\n"
"(҂`_´)\n"
"<,︻╦╤─ ҉ - - - 🤯\n"
"_/﹋\_\n")

A = (
"▄███████▄\n"
"█▄█████▄█\n"
"█▼▼▼▼▼█\n"
"██________█▌\n"
"█▲▲▲▲▲█\n"
"█████████\n"
"_████\n\n")

B = ("┈┈┏━╮╭━┓┈╭━━━━╮\n"
"┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
"┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
"┈╭━┻╮╲┗━━━━╮╭╮┈\n"
"┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
"┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
"┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
"┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")

D = ("░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄\n"
"░███████████████████████ \n"
"░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ \n"
"░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░\n"
"░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░\n"
"░░█▓▓▓▓▓▌░░░░░░░░░░\n"
"░▐█▓▓▓▓▓░░░░░░░░░░░\n"
"░▐██████▌░░░░░░░░░░\n")

E = ("╥━━━━━━━━╭━━╮━━┳\n"
"╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
"╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
"╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
"╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
"╨━━┗┛┗┛━━┗┛┗┛━━┻\n")
F = ("╔┓┏╦━╦┓╔┓╔━━╗\n" 
"║┗┛║┗╣┃║┃║X X║\n"
"║┏┓║┏╣┗╣┗╣╰╯║\n"
"╚┛┗╩━╩━╩━╩━━╝\n\n")
G = ("▬▬▬.◙.▬▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, My Friend :D \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")

H = ("┳┻┳┻╭━━━━╮╱▔▔▔╲\n"
"┻┳┻┳┃╯╯╭━┫▏╰╰╰▕\n"
"┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮\n"
"┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯\n"
"┳┻┳┻┏╯╯┃╭━╯┳━┳╯\n"
"┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲\n"
"┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕\n"
"┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱\n"
"┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯\n"
"┻┳┻┳┻┏╯▔'''╰┓┣━┳┫\n"
"┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃\n"
"┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃\n"
"┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃\n"
"┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃.\n"
"┳┻┳┻┳┻┣╋┫'''┊┣━╋┫\n"
"┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮\n"
"**I Love You 💕** \n\n")

I = ("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⣠⣾⣿⡿⠋⠀⠀⠉⠻⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠃⠀⠀⣀⡀⠀⢹⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡄⠀⠙⠻⠋⠀⠀⣸⣿⣿⠀⠀⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⣿⠟⠀⢠⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠛⠛⠒⠶⠾⢿⣿⣿⣷⣄⣾⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡀⠀⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⠀⠀⠀⠉⠉⠛⠛⠛⠶⢶⣤⣼⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠁⠀⣾⣿⣷⡄⠀⢼⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⡿⠀⠈⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣇⠀⠀⠉⠋⠁⠀⢠⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠿⢷⣤⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠉⠉⠛⢻⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⠻⣀⣀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠁⠀⣀⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣷⡀⠘⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡄⠈⢻⡇⠀⡿⠃⠀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣷⣄⢸⡇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠉⠉⠑⠒⠲⠿⢿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢺⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠉⠉⠙⠋⠀⠀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣤⣤⣀⣀⡀⠀⠀⣰⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢀⣤⡄⠀⡀⠀⢹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣿⡄⠈⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡆⠀⢹⡇⠀⠟⠁⢀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣦⣸⡇⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\n")

K = ("───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
"───█▒▒░░░░░░░░░▒▒█───\n"
"────█░░█░░░░░█░░█────\n"
"─▄▄──█░░░▀█▀░░░█──▄▄─\n"
"█░░█─▀▄░░░░░░░▄▀─█░░█\n"
"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
"█░░║║║╠─║─║─║║║║║╠─░░█\n"
"█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
"█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n\n")

L = ("░░░░▓\n"
"░░░▓▓\n"
"░░█▓▓█\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓███\n"
"░░░░██▓▓████\n"
"░░░░░██▓▓█████\n"
"░░░░░░██▓▓██████\n"
"░░░░░░███▓▓███████\n"
"░░░░░████▓▓████████\n"
"░░░░█████▓▓█████████\n"
"░░░█████░░░█████●███\n"
"░░████░░░░░░░███████\n"
"░░███░░░░░░░░░██████\n"
"░░██░          ░████\n"
"░░░░░░░░░░░░░░░░███\n"
"░░░░░░░░░░░░░░░░░░░\n\n")


N = ("────██──────▀▀▀██\n"
"──▄▀█▄▄▄─────▄▀█▄▄▄\n"
"▄▀──█▄▄──────█─█▄▄\n"
"─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
"─▀───────▀▀─▀───────▀▀\n🚶🏻‍♂️🚶🏻‍♂️ɮʏɛ ʄʀɨɛռɖֆ..")

O = ("╭━━━┳╮╱╱╭╮╱╭━━━┳━━━╮\n"
"┃╭━╮┃┃╱╭╯╰╮┃╭━╮┃╭━╮┃\n"
"┃╰━━┫╰━╋╮╭╯┃┃╱┃┃╰━━╮\n"
"╰━━╮┃╭╮┣┫┃╱┃┃╱┃┣━━╮┃\n"
"┃╰━╯┃┃┃┃┃╰╮┃╰━╯┃╰━╯┃\n"
"╰━━━┻╯╰┻┻━╯╰━━━┻━━━╯\n\n")


P = ("███████▄▄███████████▄\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓███░░░░░░░░░░░░█\n"
"██████▀░░█░░░░██████▀\n"
"░░░░░░░░░█░░░░█\n"
"░░░░░░░░░░█░░░█\n"
"░░░░░░░░░░░█░░█\n"
"░░░░░░░░░░░█░░█\n"
"░░░░░░░░░░░░▀▀\n\n")


@events.register(events.NewMessage(outgoing=True, pattern=r"\.وحش$"))
async def animmonster(monster):
    await monster.edit(A)

@events.register(events.NewMessage(outgoing=True, pattern=r"\.خنزير$"))
async def animpig(pig):
    await pig.edit(B)

@events.register(events.NewMessage(outgoing=True, pattern=r"\.قاتل$"))
async def animkiller(killer):
    await killer.edit(C)

@events.register(events.NewMessage(outgoing=True, pattern=r"\.سلاح$"))
async def animgun(gun):
    await gun.edit(D)

@events.register(events.NewMessage(outgoing=True, pattern=r"\.2كلب$"))
async def animdog(dog):
    await dog.edit(E)    

@events.register(events.NewMessage(outgoing=True, pattern=r"\.هلو$"))
async def animhello(hello):
    await hello.edit(F)

@events.register(events.NewMessage(outgoing=True, pattern=r"\.همف$"))
async def animhmf(hmf):
    await hmf.edit(G)

@events.register(events.NewMessage(outgoing=True, pattern=r"\.زوج$"))
async def couple(e):
    await e.edit(H)

@events.register(events.NewMessage(outgoing=True, pattern=r"\.رشفة$"))
async def superme(e):
    await e.edit(I)

@events.register(events.NewMessage(outgoing=True, pattern=r"\.مرحبا$"))
async def welcome(e):
    await e.edit(K)

@events.register(events.NewMessage(outgoing=True, pattern=r"\.صورة ثعبان$"))
async def snake(e):
    await e.edit(L) 

@events.register(events.NewMessage(outgoing=True, pattern=r"\.قطة$"))
async def cat(e):
    await e.edit(M)

@events.register(events.NewMessage(outgoing=True, pattern=r"\.وداعا$"))
async def bye(e):
    await e.edit(N)

@events.register(events.NewMessage(outgoing=True, pattern=r"\.شيتوز$"))
async def shitos(e):
    await e.edit(O)

@events.register(events.NewMessage(outgoing=True, pattern=r"\.دسلايك$"))
async def dislike(e):
    await e.edit(P)

@events.register(events.NewMessage(outgoing=True, pattern=f"\.هينفو$"))
async def snku(ult):
    ult = await ult.edit("`>>>`")
    animation_interval = 0.3
    animation_ttl = range(0, 15)
    await ult.edit("hypo....")
    animation_chars = [
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬛⬜⬛⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛",
        "⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬛\n⬛⬜⬛⬜⬛\n⬛⬜⬜⬜⬛\n⬛⬛⬛⬛⬛",
        "⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜",
        "[👉🔴👈])",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 15])
@events.register(events.NewMessage(pattern=f"\.squ$$"))
async def squ(ult):
    ult = await ult.edit("╔═══════════════════╗ \n  \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n \t░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ \t░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░\n╚═══════════════════╝")
    await asyncio.sleep(0.5)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░\n╚═══════════════════╝")
    await asyncio.sleep(6)


import asyncio
from telethon import events

@events.register(events.NewMessage(outgoing=True, pattern=r"^\.اقتلة(?:\s+@([\w\d_]+))?$"))
async def kiler(event):
    username = event.pattern_match.group(1)

    if username:
        try:
            user = await event.client.get_entity(f"@{username}")
            name = user.first_name  # الحصول على الاسم الأول من المنشن
        except:
            name = username  # إذا لم يُعثر عليه، استخدم نفس اليوزر
    else:
        name = "العدو"  # الاسم الافتراضي في حال عدم وجود منشن

    animation_interval = 0.5
    animation_ttl = range(7)
    DEFAULTUSER = name

    await event.edit(f"**🎯 جارِ استهداف {DEFAULTUSER}...**")

    animation_chars = [
        "🔫 *تصويب...*",
        f"__**🔫 مقاتل محترف**__ {DEFAULTUSER}       \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
        f"__**🔫 مقاتل محترف**__ {DEFAULTUSER}       \n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉  - \n _/﹋\_\n",
        f"__**🔫 مقاتل محترف**__ {DEFAULTUSER}       \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉     - \n _/﹋\_\n",
        f"__**🔫 مقاتل محترف**__ {DEFAULTUSER}       \n\n_/﹋\_\n (҂`_´)\n<,︻╦╤─ ҉        - \n _/﹋\_\n",
        f"__**🔫 مقاتل محترف**__ {DEFAULTUSER}       \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
        f"__**🔫 مقاتل محترف**__ {DEFAULTUSER}       \n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉   💥🔥 {name} سقط أرضًا!\n _/﹋\_\n",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % len(animation_chars)])

@events.register(events.NewMessage(outgoing=True, pattern=r"\.قطار$"))
async def train(ult):
    animation_interval = 0.2
    animation_ttl = range(0, 30)
    ult = await ult.edit("قطار...")
    animation_chars = [
        "**r**",
        "**ra**",
        "**rap**",
        "**rape**",
        "**rape_**",
        "**rape_t**",
        "**rape_tr**",
        "**rape_tra**",
        "**rape_trai**",
        "**rape_train**",
        "**ape_train🚅**",
        "**pe_train🚅🚃🚃**",
        "**e_train🚅🚃🚃🚃**",
        "**_train🚅🚃🚃🚃🚃**",
        "**train🚅🚃🚃🚃🚃🚃**",
        "**rain🚅🚃🚃🚃🚃🚃🚃**",
        "**ain🚅🚃🚃🚃🚃🚃🚃🚃**",
        "**in🚅🚃🚃🚃🚃🚃🚃🚃🚃**",
        "**n🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
        "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃",
        "🚃🚃🚃",
        "🚃🚃",
        "🚃",
        "**قطار**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 30])


@events.register(events.NewMessage(outgoing=True, pattern=f"\.فضائي$"))
async def alien(ult):
    animation_interval = 1
    animation_ttl = range(0, 24)
    ult = await ult.edit("اتصال.....")
    animation_chars = [
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n🚀⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛🚀⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🚀⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚀⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚀⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛🚀\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "🛸⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n🛸⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛🛸⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🛸⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🛸⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛",
        "⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛🚶‍♂️\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n👽⬛⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛👽⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛👽🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
        "__وييي....__",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 24])




@events.register(events.NewMessage(outgoing=True, pattern=r"^\.قلب( (.*)|$)"))
async def hert(ult):
    ult = await ult.edit("...")
    animation_interval = 0.5
    animation_ttl = range(0, 120)
    animation_chars = ["🖤", "❤️", "🖤", "❤️", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 4])


@events.register(events.NewMessage(outgoing=True, pattern=r"^\.حالتي( (.*)|$)"))
async def raped(ult):
    ult = await ult.edit("...")
    animation_interval = 1
    animation_ttl = range(0, 11)
    animation_chars = [
        "😁",
        "😧",
        "😡",
        "😢",
        "😁",
        "😧",
        "😡",
        "😢",
        "__هاي حالتي....__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 11])


@events.register(events.NewMessage(outgoing=True, pattern=r"^\.اني رايح( (.*)|$)"))
async def fnl(ult):
    ult = await ult.edit("...")
    animation_interval = 2
    animation_ttl = range(0, 6)
    animation_chars = ["😁🏿", "😁🏾", "😁🏽", "😁🏼", "‎😁", "بيباي نشوفكم على خير...."]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 6])


@events.register(events.NewMessage(outgoing=True, pattern=r"^\.قرد( (.*)|$)"))
async def monkey(ult):
    ult = await ult.edit("...")
    animation_interval = 2
    animation_ttl = range(0, 6)
    animation_chars = ["🐵", "🙉", "🙈", "🙊", "💥🐵💥", "نشوفكم على خير...."]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 6])

@events.register(events.NewMessage(outgoing=True, pattern=r"^\.يد( (.*)|$)"))
async def hands(ult):
    ult = await ult.edit("...")
    animation_interval = 1
    animation_ttl = range(0, 14)
    animation_chars = [
        "👈",
        "👉",
        "☝️",
        "👆",
        "👇",
        "✌️",
        "🤞",
        "🖖",
        "🤘",
        "🤙",
        "🖐️",
        "👌",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 14])


@events.register(events.NewMessage(outgoing=True, pattern=r"^\.عداد( (.*)|$)"))
async def count(ult):
    ult = await ult.edit("...")
    animation_interval = 1
    animation_ttl = range(0, 13)
    animation_chars = [
        "🔟",
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 13])

@events.register(events.NewMessage(outgoing=True, pattern=r"^\.kf$"))
async def bigf(event):
    anim = [
"""
╭━━━╮
┃╭━━╯
┃╰━━╮
┃╭━━╯
┃┃
╰╯
""","""
🌕🌕🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕🌕🌕
🌕🌕
🌕🌕
🌕🌕🌕🌕🌕
🌕🌕🌕🌕🌕
🌕🌕
🌕🌕
🌕🌕
🌕🌕
""", """
🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿
🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿
🇺🇿🇺🇿
🇺🇿🇺🇿
🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿
🇺🇿🇺🇿🇺🇿🇺🇿🇺🇿
🇺🇿🇺🇿
🇺🇿🇺🇿
🇺🇿🇺🇿
🇺🇿🇺🇿
""", """
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️
❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️
❤️❤️
❤️❤️
❤️❤️
"""]
    an = random.choice(anim)
    return await event.edit(an)

@events.register(events.NewMessage(outgoing=True, pattern=r"^\.f (.*)"))
async def payf(e):
    paytext = e.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 5,
        paytext * 5,
        paytext * 1,
        paytext * 1,
        paytext * 4,
        paytext * 4,
        paytext * 1,
        paytext * 1,
        paytext * 1,
    )
    await e.edit(pay)


@events.register(events.NewMessage(outgoing=True, pattern=r"^\.توقف_كبير$"))
async def bigof(event):
    await event.edit(".")
    time.sleep(0.3)
    await event.edit("..")
    time.sleep(0.3)
    await event.edit("...")
    animation_interval = 0.1
    animation_ttl = range(0, 7)
    await event.edit(
        "┏━━━┓╋╋╋╋┏━━━┓ \n┃┏━┓┃╋╋╋╋┃┏━┓┃ \n┃┃╋┃┣┓┏┓┏┫┃╋┃┃ \n┃┃╋┃┃┗┛┗┛┃┃╋┃┃ \n┃┗━┛┣┓┏┓┏┫┗━┛┃ \n┗━━━┛┗┛┗┛┗━━━┛"
    )
    animation_chars = [
        "╭━━━╮╱╱╱╭━╮ \n┃╭━╮┃╱╱╱┃╭╯ \n┃┃╱┃┣━━┳╯╰╮ \n┃┃╱┃┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃┃┃ \n╰━━━┻━━╯╰╯ ",
        "╭━━━╮╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃┃┃ \n ╰━━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 7])


@events.register(events.NewMessage(outgoing=True, pattern=r"^\.flower$"))
async def flower(event):
    await event.edit(".")
    time.sleep(0.3)
    await event.edit("..")
    time.sleep(0.3)
    await event.edit("...")
    time.sleep(0.3)
    await event.edit("ㅤ\n         ▒▒▒▒▒▒▒▒▒\n      ▒▒▒▒▒▒▒▒▒▒▒▒\n  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒\n▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒\n▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒\n▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒\n  ▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒\n    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n       ▒▒▒▒▒▒▒▒▒▒▒▒▒\n         ▒▒▒▒▒▒▒▒▒▒\n              ▒▒▒▒▒▒\n                     ▓\n     ▓▓▓       ▓\n ▓▓▓▓▓▓  ▓\n▓▓            ▓▓\n ▓                 ▓     ▓▓▓▓▓\n ▓                 ▓     ▓▓▓▓▓\n                     ▓   ▓▓▓▓▓▓\n                     ▓▓           ▓▓\n                     ▓               ▓\n                     ▓\n     ████████████\n         █████████\n            ███████\n             ██████\n.................███..............\n")
        
        
        
@events.register(events.NewMessage(outgoing=True, pattern=r"^\.vheart ?(.*)"))
async def vheart(event):
    await event.edit(".")
    time.sleep(0.3)
    await event.edit("..")
    time.sleep(0.3)
    await event.edit("...")
    time.sleep(0.3)
    await event.edit("..........###########\n......##############\n....################\n..##################.............########\n...##################.......#############\n....##################.....##############\n.....#################...################\n.......#################################\n.........###############################\n...........#############################\n..............##########################\n................########################\n...................#####################\n.....................##################\n.......................###############\n........................#############\n..........................##########\n...........................########\n............................######\n.............................#####\n..............................###\n...............................#")
  
 
 
@events.register(events.NewMessage(outgoing=True, pattern=r"^\.luvart$"))
async def luvart(event):
    await event.edit(".")
    time.sleep(0.3)
    await event.edit("..")
    time.sleep(0.3)
    await event.edit("...")
    time.sleep(0.3)
    await event.edit("✨✨✨✨✨✨✨✨✨✨✨✨✨\n✨✨✨💖💖💖💖💖💖💖✨✨✨\n✨✨✨✨✨💖💖💖✨✨✨✨✨\n✨✨✨✨✨💖💖💖✨✨✨✨✨\n✨✨✨✨✨💖💖💖✨✨✨✨✨\n✨✨✨✨✨💖💖💖✨✨✨✨✨\n✨✨✨💖💖💖💖💖💖💖✨✨✨\n✨✨✨✨✨✨✨✨✨✨✨✨✨\n💖💖💖💖💖💖💖💖💖💖💖💖💖\n💖💖✨✨✨💖💖💖✨✨✨💖💖\n💖✨✨✨✨✨💖✨✨✨✨✨💖\n💖✨✨✨✨✨✨✨✨✨✨✨💖\n💖💖✨✨✨✨✨✨✨✨✨💖💖\n💖💖💖✨✨✨✨✨✨✨💖💖💖\n💖💖💖💖✨✨✨✨✨💖💖💖💖\n💖💖💖💖💖✨✨✨💖💖💖💖💖\n💖💖💖💖💖💖✨💖💖💖💖💖💖\n💖💖💖💖💖💖💖💖💖💖💖💖💖\n✨✨✨✨✨✨✨✨✨✨✨✨✨\n✨✨💖💖✨✨✨✨✨💖💖✨✨\n✨✨💖💖✨✨✨✨✨💖💖✨✨\n✨✨💖💖✨✨✨✨✨💖💖✨✨\n✨✨💖💖✨✨✨✨✨💖💖✨✨\n✨✨💖💖💖✨✨✨💖💖💖✨✨\n✨✨💖💖💖💖💖💖💖💖💖✨✨\n✨✨✨💖💖💖💖💖💖💖✨✨✨\n✨✨✨✨✨✨✨✨✨✨✨✨✨\nㅤ")
