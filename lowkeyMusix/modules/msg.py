
import os
from lowkeyMusix.config import SOURCE_CODE
from lowkeyMusix.config import ASSISTANT_NAME
from lowkeyMusix.config import PROJECT_NAME
from lowkeyMusix.config import SUPPORT_GROUP
from lowkeyMusix.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Heyoo 👋 [{}](tg://user?id={})!**\n\n bot ini dibuat untuk memutar music VCG/OBRALAN SUARA di Telegram Groups & Channels.\n\n 👑ketik /help untuk info lebih lanjut."
      HELP_MSG  = [
        ".",
f"""
**Heyooo 👋  Selamat datang kembali di{PROJECT_NAME}

✣️ {PROJECT_NAME} dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah.

✣️ Assistant Music » @{ASSISTANT_NAME}\n\nKlik Next untuk instruksi**

""",

f"""
**Pengaturan**

**untuk group Music **
1. Jadikan bot sebagai admin di group dan tambahkna "fitur add new admin"
2. Mulai obrolan suara / VCG
3. Ketik `/userbotjoin` dan coba /play <nama lagu>
× Jika Assistant Bot bergabung selamat menikmati musik, 
× Jika Assistant Bot tidak bergabung Silahkan Tambahkan @{ASSISTANT_NAME} ke grup Anda dan coba lagi

**untuk Channel Music **
1) jadikan admin di channel
2) kirim /userbotjoinchannel di linked group
3) sekarang kirim perintah in linked group
""",
f"""
**perintah**

**=>> memutar music 🎧**

- /play: memutar lagu yang di request
- /play [yt url] : memutar dengan url dari youtube
- /play [reply yo audio]: memutar audio yang di reply
- /splay: memutar lagu via jio saavn
- /ytplay: memutar via Youtube Music

**=>> Playback ⏯**

- /player: buka Setting menu 
- /skip: Skips lagu yang sedang di putar
- /pause: Pause lagu yang sedang di putar
- /resume: memulai lagi yang di paused 
- /end: Stops media playback
- /current: menampilkan informasi lagu yang sedang di putar
- /playlist: menampilkan playlist lagu yang sedang di putar

* perintah dari member kecuali /play, /current  and /playlist  hanya untuk admins di group.
""",

f"""
**=>> Channel Music Play 🛠**

⚪️ untuk linked group admins only:

- /cplay [song name] - play song you requested
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you dont like to play in linked group:

1) cari channel ID.
2) buat group dengan judul: Channel Music: your_channel_id
3) tambahkan bot dengan full permissions
4) tambahkan @{ASSISTANT_NAME} ke channel dan jadikan admin.
5) kirim perintah ke group yang terhubung. (ingat untuk menggunakan /ytplay instead /play)
""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
f"""
**=>> Song Download 🎸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**=>> Search Tools 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: untuk mencari lyrics
- /lirik [song name]: untuk mencari lyrics
""",

f"""
**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
