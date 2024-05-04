import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

API_ID = int(getenv("API_ID", "27424332"))  # Optional
API_HASH = getenv("API_HASH", "cb93e76ed8e78c8081f52cd3aa66f08b")  # Optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5348648456").split()))
OWNER_ID = int(getenv("OWNER_ID", "6099950428"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://sagar121:sagar121@sagar1.ql1togl.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6032040315:AAFyBtAEBGf3RDgl-DjSiQUejFexmeDDnDI")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://te.legra.ph/file/f49043ee43b5f4b96b697.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", ('👑Official Account😊\n'
                                    '\n'
                                    '💟Wish Me On 20 Dec 🎂\n'
                                    '\n'
                                    '⚡My Life My Rules💪\n'
                                    '\n'
                                    '🎶Music ka Diwana💥\n'
                                    '\n'
                                    '🕉️Mahadev Bhakt🕉️\n'
                                    '\n'
                                    '♍I’m not Rich ßut I’m Royal 👑\n'
                                    '\n'
                                    '༒︎ɪɴsᴛᴀ ɪᴅ༒︎ @govind_official_mp'))
PM_LOGGER = getenv("PM_LOGGER", "-1001401958446")
LOG_GROUP = getenv("LOG_GROUP", "-1001401958446")
GIT_TOKEN = getenv("GIT_TOKEN")  # Personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/GOVIND-BOTS/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master")  # Don't change

# Multiple STRING_SESSION variables
STRING_SESSION1 = getenv("STRING_SESSION1", "BQB6i7iDBgEWixewyrUpehYp9OMs94P4F4JN__FBFrdW8tNmsKe41fKqZa2lOxHE9Hp9WUJxPHd0y_Hnr-eI0b6vDyBXUC1QHrUHOu7r45qAfY-wDeLaJxlM193WgGinaDbQbJ2v2x3wMs0w1-csufMwXt_BCKhFovDJqGqTgVBpibMKyTVM_b-nP4cPwyf-6t3k0VBIZlXQmOz1UC8V2TGGOD7eb7FAC101CD537isNh3dBzXQOE-xt_04XKvTghccbM_-QaSShUuJINI_toNCUU6JrwSS8gO2rzp3qnD9E2YRKsIhWTxllgq_Z0ToQgDRWBP_wZw3PU05pmoeg3KZ-AAAAAWuV21wA")
# Repeat the above line for STRING_SESSION2 through STRING_SESSION10 as needed

