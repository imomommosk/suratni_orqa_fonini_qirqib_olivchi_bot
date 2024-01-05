from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from loader import dp


@dp.message_handler(Command("info"))
async def bot_start(message: types.Message):
    await message.answer(f"{message.from_user.full_name}!")
