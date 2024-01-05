from aiogram import types

from loader import dp

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp
from googletrans import Translator

tarjima = Translator()
# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    matn = message.text
    matn1 = tarjima.translate(matn, dest='en')
    matn2 = matn1.text
    await message.reply(matn2)