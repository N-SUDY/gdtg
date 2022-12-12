import os, logging, asyncio
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from pyromod import listen
import pymongo
from pymongo import MongoClient

class Creds:
 TEAMDRIVE_FOLDER_ID = ""
 TEAMDRIVE_ID = ""

class Config(object):
  BOT_TOKEN = '5705156853:AAETn1HpOHb0POCFGqUCwGOLyVHVN0qR_rM'
  API_ID = '17894641'
  API_HASH = '4e5b39e5c7c6066e5144dfc50cf466cf'
  DOWNLOAD_DIR = 'downloads'
  AUTH_USERS = [1349301822, 5468192421]
  DATABASE_URL = str("postgres://ihrsawqm:EiUg6VXSWiuy1yr2Cps_-jF0uKu1Jped@arjuna.db.elephantsql.com/ihrsawqm")
  USERNAME = "gdtg"

LOG_FILE_NAME = "Gdrive-Bot@Log.txt"

if os.path.exists(LOG_FILE_NAME):
    with open(LOG_FILE_NAME, "r+") as f_d:
        f_d.truncate(0)

cluster = MongoClient(Config.DATABASE_URL)
db = cluster[Config.USERNAME]
col = db["data"]
td = db["teamdrive"]

data = []
list_handler = []

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=2097152000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
LOGS = logging.getLogger(__name__)


bot = Client("gdrive-bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN, workers=2)

if not Config.DOWNLOAD_DIR.endswith("/"):
  Config.DOWNLOAD_DIR = str() + "/"
if not os.path.isdir(Config.DOWNLOAD_DIR):
  os.makedirs(Config.DOWNLOAD_DIR)
