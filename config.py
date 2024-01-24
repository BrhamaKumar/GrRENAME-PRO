import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20810825")

API_HASH = os.environ.get("API_HASH", "707e67f53b4593a3e9b6b424311f84d0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6763124124:AAEtLk_bprWNGmM2lUpoXPQCHArkoJSJMLE") 

FORCE_SUB = os.environ.get("FORCE_SUB", "demosaveforce") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://zoey972897:yDLALohi1EugzN9F@cluster0.ifj2lkp.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/3e4d4d7361cef908dc23f.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6301693754').split()]

