from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# ! Start
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)

free_games = KeyboardButton('/free')

start_kb.add(free_games)