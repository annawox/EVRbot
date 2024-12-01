from aiogram import types

async def handle_message(message: types.Message):
    if message.text == "/start":
        await message.answer("Привет! Я помогаю проверять проекты")
    else:
        await message.answer("Не понимаю, попробуйте снова")
