import logging

from aiogram import Bot, Dispatcher, executor, types

import config
import validation

API_TOKEN = config.API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Hello message"""
    await message.reply("Здравствуйте! Этот бот создан для отправки ошибок с  вашегоустройства.\n Для начала работы"
                        "отправьте сообщением ваш id, указанный в профиле на сайте multimer.ru")


@dp.message_handler()
async def echo(message: types.Message):
    """receives user's id"""
    if validation.valid_id(message.text):
        await message.answer(f"Вы указали id {message.text}")
    else:
        await message.answer(f"Id должен быть цифрой или числом!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
