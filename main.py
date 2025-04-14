import asyncio
from loader import dp, bot

async def main():

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()





if __name__ == '__main__':
    asyncio.run(main())