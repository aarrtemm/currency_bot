import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SQLALCHEMY_URL = os.getenv("SQLALCHEMY_URL")
