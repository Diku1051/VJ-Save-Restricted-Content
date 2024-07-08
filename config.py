import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "2207680"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8172d048fba05da1618f3968602a9545")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://iipmqspr:O12ivDv6iHk9LDdq@cluster0.syv8ui7.mongodb.net/")
