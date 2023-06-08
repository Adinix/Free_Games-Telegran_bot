from dp_bot import bot
from json import load, dump
import module.free_games_steam as free_steam
from aiogram.utils.exceptions import ChatNotFound
from aiogram import types
import asyncio
from keyboards.inline_keyboards import get_games


# ! Function
#* Save settings
async def settings_server_apply(id, setting, value):
    try:
        with open('config.json', 'r') as f:
            config = load(f)

        server_cfg = config[str(id)]

        server_cfg[setting] = value

        config[str(id)] = server_cfg

        with open('config.json', 'w') as f:
            dump(config, f, indent=4, ensure_ascii=False)

        return None
    except KeyError:
        return f'Error: No dict id_server (KeyError: "{id}")'



#* Get settings
async def settings_server_get(id):

    with open('config.json', 'r') as f:
        config = load(f)

    server_cfg = config[str(id)]

    return server_cfg



# ?  Tyming
async def potok_typing_000seconds():

    with open('config.json', 'r') as f:
        config = load(f)

    list_free_games_steam = config['free_games_steam']

    free_games = free_steam.free_games()
    free_games_img = free_games[1]
    free_games = free_games[0]

    now_list_free_games_steam = free_steam.free_games()[0]

    for i in now_list_free_games_steam:
        if not i in list_free_games_steam:
            for k in config:
                try:
                    await bot.send_message(chat_id=k, text=f'💙 Новая бесплатная игра в Steam! 💛\n<a href="{free_games_img[i]}"> </a><b>{i}</b>',
                                            parse_mode=types.ParseMode.HTML, reply_markup=get_games(free_games[i]))
                except ChatNotFound:
                    pass

            list_free_games_steam.append(i)


    config['free_games_steam'] = list_free_games_steam

    with open('config.json', 'w') as f:
        dump(config, f, indent=4, ensure_ascii=False)

    await asyncio.sleep(3600)

    await potok_typing_000seconds()
    asyncio.create_task(potok_typing_000seconds())