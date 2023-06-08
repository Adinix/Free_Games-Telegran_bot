from dp_bot import dp, bot
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.inline_keyboards import get_games, choice_platform
from keyboards import start_kb
import module.free_games_steam as free_steam
from json import load, dump


dict_msg_id = dict()


# @dp.message_handler(commands='start')
async def start(message: types.Message):

    await message.answer(text=f'Добро пожаловать!\n\
Я вам сам сообщю, когда появятся бесплатные игры.\n\
Так же вы можете написать команду /free, что бы увидеть все бесплатные игры которые мне удалось обнаружить.\n\
Если что то не понятно пишите команду /help.',
                                    reply_markup=start_kb)

    with open('config.json', 'r') as f:
        config = load(f)

    try:
        if config[str(message.chat.id)]: pass
    except KeyError:

        config[message.chat.id] = {'post_message': True}

        with open('config.json', 'w') as f:
            dump(config, f, indent=4, ensure_ascii=False)



# @dp.message_handler(commands='help')
async def help(message: types.Message):

    await message.answer(text='Помогаю...\nСкоро будет!')



# @dp.message_handler(commands='free')
async def free(message: types.Message):

    global dict_msg_id

    message_temp = await message.answer(text='<b>Выберете платворму:</b>', 
                                        parse_mode=types.ParseMode.HTML, 
                                        reply_markup=choice_platform(message.from_user.id))
    dict_msg_id[message_temp.chat.id] = message_temp.message_id



# @dp.callback_query_handler(lambda a: a.data.startswith('choice_platform_'))
async def call_choice_platform(call: types.CallbackQuery):

    platform = call.data.split(' ')[0].split('_')[-1]
    user_id = call.data.split(' ')[-1].strip(' ')

    if int(user_id) == call.from_user.id:

        if platform == 'steam':
            await call.answer(text=f'🔎 Поиск бесплатных игор в Steam...')

            free_games = free_steam.free_games()
            free_games_img = free_games[1]
            free_games = free_games[0]

            lf = len_free_games = len(free_games)

            async def msg_temp_1(num):
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=dict_msg_id[call.message.chat.id],
                                            text=(f'{num} бесплатная игра в Steam!'))

            async def msg_temp_2_4(num):
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=dict_msg_id[call.message.chat.id],
                                            text=(f'{num} бесплатные игры в Steam!'))

            async def msg_temp_5_9(num):
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=dict_msg_id[call.message.chat.id],
                                            text=(f'{num} бесплатных игор в Steam!'))

            if lf == 0:
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=dict_msg_id[call.message.chat.id],
                                            text=(f'😞 Пока что нет бесплатных игор в Steam!'))
            elif lf == 1: msg_temp_1('1️⃣')
            elif lf == 2: msg_temp_2_4('2️⃣')
            elif lf == 3: msg_temp_2_4('3️⃣')
            elif lf == 4: msg_temp_2_4('4️⃣')
            elif lf == 5: msg_temp_5_9('5️⃣')
            elif lf == 6: msg_temp_5_9('6️⃣')
            elif lf == 7: msg_temp_5_9('7️⃣')
            elif lf == 8: msg_temp_5_9('8️⃣')
            elif lf == 9: msg_temp_5_9('9️⃣')
            else: msg_temp_5_9(lf)

            dict_msg_id.pop(call.message.chat.id)

            for i in free_games:
                await bot.send_message(chat_id=call.message.chat.id, text=f'🎮<a href="{free_games_img[i]}"> </a><b>{i}</b>',
                                        parse_mode=types.ParseMode.HTML, reply_markup=get_games(free_games[i]))


        elif platform == 'epicgames':
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=dict_msg_id[call.message.chat.id],
                                            text=('😞 Пока что этой функции нету!'))

    else:
        await bot.send_message(chat_id=call.message.chat.id, 
                                text=f'⚠️ @{call.from_user.username} инзвините, на кнопку должен нажать тот кто вызвал команду!')



# @dp.message_handler(commands='get_chat_id')
# async def get_chat_id(msg: types.Message):
#     await msg.answer(text=f'<b>Chat id:\n{msg.chat.id}</b>', parse_mode=types.ParseMode.HTML)



def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(help, commands='help')
    dp.register_message_handler(free, commands='free')
    dp.register_callback_query_handler(call_choice_platform, lambda a: a.data.startswith('choice_platform_'))
    # dp.register_message_handler(get_chat_id, commands='get_chat_id')