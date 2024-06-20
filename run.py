from asyncio import run
from logging import basicConfig, INFO
from os import getenv

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv

from app.database.models import async_main
from app.handlers import router


async def on_startup() -> None:
    load_dotenv()
    await async_main()
    basicConfig(level=INFO)
    bot = Bot(token=getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        run(on_startup())
    except KeyboardInterrupt:
        print('Bot ended')
