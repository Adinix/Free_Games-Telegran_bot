from dp_bot import dp
from aiogram.utils import executor
from module.function import potok_typing_000seconds
import asyncio


# ! Запускаеться при старте
async def on_startup(_):
    asyncio.create_task(potok_typing_000seconds())


    print('Bot Start!')

# ! Подключаем хендлеры
from handlers import client

client.register_message_handlers(dp)


# ! Запускаем бота
if __name__ == '__main__':
    executor.start_polling(
                            dp,
                            skip_updates=True,
                            on_startup=on_startup
                            )