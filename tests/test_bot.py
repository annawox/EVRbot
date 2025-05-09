import pytest
from bot.handlers import handle_message
from aiogram.types import Message


# Пример теста для обработчика сообщений
@pytest.mark.asyncio
async def test_handle_start():
    message = Message(text="/start")
    response = await handle_message(message)
    assert response.text == "Привет! Я помогаю проверять проекты."
