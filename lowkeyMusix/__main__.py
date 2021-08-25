

import requests
from pyrogram import Client as Bot

from lowkeyMusix.config import API_HASH
from lowkeyMusix.config import API_ID
from lowkeyMusix.config import BG_IMAGE
from lowkeyMusix.config import BOT_TOKEN
from lowkeyMusix.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="lowkeyMusix.modules"),
)

bot.start()
run()
