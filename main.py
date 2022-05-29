import logging

from aiogram import Bot, Dispatcher, executor, types

import config
import error_receiver as er

API_TOKEN = config.API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message) :
    """Hello message"""
    await message.reply("Здравствуйте! Этот бот создан для отправки ошибок с  вашего устройства.\n"
                        "Бот уже привязал ваш аккаунт к кондиционеру и успешно работает.")


@dp.message_handler()
async def echo(message: types.Message) :
    await message.answer(f"Этот бот не принимает сообщения, он отправляет ошибки устройств.")


async def send_error():
    """Send error message"""
    while True :
        error = er.receive(er.client)
        if error:
            for i in error:  # error is {telegram_id:error_message}
                await bot.send_message(chat_id=error[i], text=error[i])


async def on_startup(x):
    asyncio.create_task(is_enabled())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
