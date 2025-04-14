import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage

from handlers import start, user
from middlewares.throttling import ThrottlingMiddleware

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

REDIS_USER = os.getenv('REDIS_USER')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

storage = RedisStorage.from_url(f'redis://{REDIS_USER}:{REDIS_PASSWORD}@redis:6379',
                                connection_kwargs={"decode_responses": True})

BOT_TOKEN = os.getenv('BOT_TOKEN')

dp = Dispatcher(storage=storage)
dp.message.filter(F.chat.type == "private")

dp.message.middleware(ThrottlingMiddleware())

dp.include_router(start.router)
dp.include_router(user.router)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
