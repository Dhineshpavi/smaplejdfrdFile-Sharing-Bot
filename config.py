#(©)@DP_BOTZ
#don't remove credit @DP_BOTZ 




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7438023087:AAEGkg9pfJ4gi4G1AiRIkoRpI7ZU37P6GlQ")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "11973721"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002016963150"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1242556540"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://evamusicbot:mrwaris04@cluster0.5ad8zuj.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "DPBOTZDEVELOPER")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001914687456"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝐇𝐞𝐥𝐥𝐨 👋 {first} ✨ 𝐈 𝐜𝐚𝐧 𝐒𝐭𝐨𝐫𝐞 𝐓𝐚𝐦𝐢𝐥 𝐃𝐮𝐛𝐛𝐞𝐝 𝐀𝐧𝐢𝐦𝐞 𝐅𝐢𝐥𝐞𝐬 ✨ & 𝐎𝐭𝐡𝐞𝐫 𝐔𝐬𝐞𝐫𝐬 𝐂𝐚𝐧 𝐀𝐜𝐜𝐞𝐬𝐬 𝐈𝐭 𝐟𝐫𝐨𝐦 𝐒𝐩𝐞𝐜𝐢𝐚𝐥 𝐋𝐢𝐧𝐤")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1242556540").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐡𝐞𝐥𝐥𝐨 - {username} 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 👍 𝐍𝐞𝐱𝐭 𝐂𝐥𝐢𝐜𝐤 , 𝐓𝐫𝐲 𝐚𝐠𝐚𝐢𝐧 ✅")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌𝐃𝐨𝐧'𝐭 𝐬𝐞𝐧𝐝 𝐦𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐝𝐢𝐫𝐞𝐜𝐭𝐥𝐲 𝐈'𝐦 𝐨𝐧𝐥𝐲 𝐅𝐢𝐥𝐞 𝐒𝐡𝐚𝐫𝐞 𝐛𝐨𝐭 ❗ 𝐲𝐨𝐮 𝐍𝐞𝐞𝐝 𝐎𝐰𝐧 𝐁𝐨𝐭 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐲 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫💙"

ADMINS.append(OWNER_ID)
ADMINS.append(5136853481)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
