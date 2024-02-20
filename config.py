import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "27424332")) #optional
API_HASH = getenv("API_HASH", "cb93e76ed8e78c8081f52cd3aa66f08b") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5348648456").split()))
OWNER_ID = int(getenv("OWNER_ID", "6099950428"
MONGO_URL = getenv("MONGO_URL","mongodb+srv://sagar121:sagar121@sagar1.ql1togl.mongodb.net/?retryWrites=true&w=majority"
BOT_TOKEN = getenv("BOT_TOKEN", "6032040315:AAFyBtAEBGf3RDgl-DjSiQUejFexmeDDnDI")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://te.legra.ph/file/f49043ee43b5f4b96b697.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT", '👑Official Account😊

💟Wish Me On 20 Dec 🎂

⚡My Life My Rules💪

🎶Music ka Diwana💥

🕉️Mahadev Bhakt🕉️

♍I’m not Rich ßut I’m Royal 👑

༒︎ɪɴsᴛᴀ ɪᴅ༒︎ @govind_official_mp"
PM_LOGGER = getenv("PM_LOGGER","-1001401958446"
LOG_GROUP = getenv("LOG_GROUP","-1001401958446"
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQB6i7iDBgEWixewyrUpehYp9OMs94P4F4JN__FBFrdW8tNmsKe41fKqZa2lOxHE9Hp9WUJxPHd0y_Hnr-eI0b6vDyBXUC1QHrUHOu7r45qAfY-wDeLaJxlM193WgGinaDbQbJ2v2x3wMs0w1-csufMwXt_BCKhFovDJqGqTgVBpibMKyTVM_b-nP4cPwyf-6t3k0VBIZlXQmOz1UC8V2TGGOD7eb7FAC101CD537isNh3dBzXQOE-xt_04XKvTghccbM_-QaSShUuJINI_toNCUU6JrwSS8gO2rzp3qnD9E2YRKsIhWTxllgq_Z0ToQgDRWBP_wZw3PU05pmoeg3KZ-AAAAAWuV21wA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQB6i7iDBgEWixewyrUpehYp9OMs94P4F4JN__FBFrdW8tNmsKe41fKqZa2lOxHE9Hp9WUJxPHd0y_Hnr-eI0b6vDyBXUC1QHrUHOu7r45qAfY-wDeLaJxlM193WgGinaDbQbJ2v2x3wMs0w1-csufMwXt_BCKhFovDJqGqTgVBpibMKyTVM_b-nP4cPwyf-6t3k0VBIZlXQmOz1UC8V2TGGOD7eb7FAC101CD537isNh3dBzXQOE-xt_04XKvTghccbM_-QaSShUuJINI_toNCUU6JrwSS8gO2rzp3qnD9E2YRKsIhWTxllgq_Z0ToQgDRWBP_wZw3PU05pmoeg3KZ-AAAAAWuV21wA")
STRING_SESSION3 = getenv("STRING_SESSION3", "BQB6i7iDBgEWixewyrUpehYp9OMs94P4F4JN__FBFrdW8tNmsKe41fKqZa2lOxHE9Hp9WUJxPHd0y_Hnr-eI0b6vDyBXUC1QHrUHOu7r45qAfY-wDeLaJxlM193WgGinaDbQbJ2v2x3wMs0w1-csufMwXt_BCKhFovDJqGqTgVBpibMKyTVM_b-nP4cPwyf-6t3k0VBIZlXQmOz1UC8V2TGGOD7eb7FAC101CD537isNh3dBzXQOE-xt_04XKvTghccbM_-QaSShUuJINI_toNCUU6JrwSS8gO2rzp3qnD9E2YRKsIhWTxllgq_Z0ToQgDRWBP_wZw3PU05pmoeg3KZ-AAAAAWuV21wA")
STRING_SESSION4 = getenv("STRING_SESSION4", "BQB6i7iDBgEWixewyrUpehYp9OMs94P4F4JN__FBFrdW8tNmsKe41fKqZa2lOxHE9Hp9WUJxPHd0y_Hnr-eI0b6vDyBXUC1QHrUHOu7r45qAfY-wDeLaJxlM193WgGinaDbQbJ2v2x3wMs0w1-csufMwXt_BCKhFovDJqGqTgVBpibMKyTVM_b-nP4cPwyf-6t3k0VBIZlXQmOz1UC8V2TGGOD7eb7FAC101CD537isNh3dBzXQOE-xt_04XKvTghccbM_-QaSShUuJINI_toNCUU6JrwSS8gO2rzp3qnD9E2YRKsIhWTxllgq_Z0ToQgDRWBP_wZw3PU05pmoeg3KZ-AAAAAWuV21wA")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
