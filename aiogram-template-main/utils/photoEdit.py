import aiohttp
from aiogram import types
from io import BytesIO
from loader import bot

async def photo_link(photo: types.photo_size.PhotoSize) -> str:
    with await photo.download(BytesIO()) as file:
        form = aiohttp.FormData()
        form.add_field(
            name='file',
            value=file,
        )

        async with bot.session.post('https://telegram.ph/upload', data=form) as response:
            img_scr = await response.json()
            print(img_scr)
        link ='https://telegram.ph/' + img_scr[0]["scr"]
        return link