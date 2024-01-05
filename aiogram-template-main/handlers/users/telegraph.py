from aiogram import types
from loader import dp
from numpy import msg
from utilist import photo_link
from utilist import remove_background

@dp.message_handler(content_types='photo')
async def send_photo(message: types.Message):
    photo = msg.photo[-1]
    link = await photo_link(photo)
    await msg.answer(link)


    new_photo = await remove_background(link)
    await msg.reply_document(document=new_photo, caption="Orqa fon olindi")