from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="YOUR_TOKEN") !!!!!!!!!!!!!!!!!!!!!!!!!!!!
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Отправьте мне файл или архив для проверки.")

if __name__ == "__main__":
    executor.start_polling(dp)
