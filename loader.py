import logging
import os

from aiogram import Bot, Dispatcher

BOT_TOKEN = os.getenv('BOT_TOKEN')

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)