import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.filters import Command

from database.models import  async_main
import func
import set
from config import API_TOKEN

async def startup(bot: Bot):
    await bot.send_message(6512093052, 'Salom Bot Ishga Tushdi')

async def shutdown(bot: Bot):
    await bot.send_message(6512093052, "Bot Ishdan To'xtadi")

async def main():
    await async_main()
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    
    dp.message.register(func.cmd_start, Command('start'))
    dp.message.register(func.get_help, Command('help'))
    dp.message.register(func.get_news, Command('news'))
    dp.message.register(set.set_contact)
    dp.message.register(set.set_language)
    dp.message.register(set.set_role)
    await bot.set_my_commands([
        BotCommand(command='/start', description='Botni ishga tushirish'),
        BotCommand(command='/register', description="Ro'yhatdan o'tish"),
        BotCommand(command='/help', description='Yordam'),
        BotCommand(command='/news', description='Eng muhim yangliklar')
    ])
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
