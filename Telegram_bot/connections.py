import telebot
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv('.env')

bot = telebot.TeleBot(os.environ["API"])

conn = psycopg2.connect(
    host = os.environ["host"],
    user = os.environ["user"],
    password = os.environ["password"],
    port = os.environ["port"],
    dbname = os.environ["dbname"]
)
