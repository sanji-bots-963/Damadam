import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27390437")
    API_HASH  = os.environ.get("API_HASH", "8dcef0252047d3a4556ad80280db4146")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7352327938:AAGNcwGEIIhrRFSc3IpQjpkkJBmEr0EThsE") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","SH_METADATA_RENAMER_BOT")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://sagatobots00001:sagatobots100@cluster00001.vgdshkw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster00001")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph//file/a9a177e24269cd69cb4fe.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6727550037').split()]

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Straw_Hat_Bots") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002031978775"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.

➻ You Can Also Convert Video To File And File To Video.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.

<b>Bot Is Made By :</b> @Straw_Hat_Bots"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/Straw_Hat_Bots>Straw Hat Bots</a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/urr_sanjii_robot>Sanji Sama</a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>📊 Build Version</b> : <a href=https://instagram.com/jishu.editz>Rename v4.5.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/Straw_Hat_Bots>Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `zorosan110@axl`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>-map 0 -c:s copy -c:a copy -c:v copy -metadata title="Encoded By :- @Straw_Hat_Bots" -metadata author="@Straw_Hat_Bots" -metadata:s:s title="Subtitled By :- @Straw_Hat_Bots" -metadata:s:a title="By :- @Straw_Hat_Bots" -metadata:s:v title="Encoded By :- @Straw_Hat_Bots"</code>

💬 For Any Help Contact @Straw_Hat_Bots
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
