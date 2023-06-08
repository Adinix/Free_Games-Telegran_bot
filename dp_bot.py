from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from os import getenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)