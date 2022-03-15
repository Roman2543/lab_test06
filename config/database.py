from pymongo import MongoClient
import ssl
from core import config

ssl._create_default_https_context = ssl._create_unverified_context



client = MongoClient("mongodb+srv://"+config.setting.user_name+":"+config.setting.pass_word+":@"+config.setting.host+":/myFirstDatabase?retryWrites=true&w=majority", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)


db = client.todo_app

students_collection = db["students"]

