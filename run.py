import asyncio
import datetime
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import parse
from handlers import router


import config
from database import settings, requests as req


async def run():
    await settings.init_db()
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


async def parse_rate():
    while True:
        data = parse.get_exchange_rate()
        await req.create_new_rate(data, datetime.datetime.now())
        await asyncio.sleep(30)


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        await asyncio.gather(run(), parse_rate())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")

if __name__ == '__main__':
    asyncio.run(main())
