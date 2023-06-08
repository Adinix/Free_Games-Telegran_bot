from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# ! Choice platform
def choice_platform(user_id):
    choice_platform = InlineKeyboardMarkup()

    steam = InlineKeyboardButton(text='Steam', callback_data=f'choice_platform_steam {user_id}')
    epicgames = InlineKeyboardButton(text='EpicGames', callback_data=f'choice_platform_epicgames {user_id}')

    choice_platform.add(steam, epicgames)

    return choice_platform



# ! Get games is platform
def get_games(url):

    get_games = InlineKeyboardMarkup()

    game = InlineKeyboardButton(text='Получить!', url=url)

    get_games.add(game)

    return get_games