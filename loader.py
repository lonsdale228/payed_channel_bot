import logging
import os

from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)


