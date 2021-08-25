import requests
from pyrogram import Client
from lowkeyMusix.config import BOT_USERNAME
from lowkeyMusix.helpers.filters import command


@Client.on_message(command(["lyric","lirik", f"lyric@{BOT_USERNAME}"]))
async def lirik(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**ketik liriknya juga boti !**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("🔎 seme ngangkang sabar anjir lagi nyari...")
        resp = requests.get(f"https://tede-api.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit("**lu cari lirik apaan kgk tau gw bencong .** coba judulnya benerin !")
