from aiogram import types
from bot.utils import analyze_code_with_model

def format_response(response):
    """
    Форматирует ответ, полученный от модели.
    :param response: Ответ от модели в формате JSON
    :return: Отформатированный текст
    """
    if "choices" in response and len(response["choices"]) > 0:
        return f"Ответ: {response['choices'][0]['message']['content']}"
    else:
        return "Не удалось получить результат анализа."

async def handle_document(message: types.Message):
    """
    Обрабатывает файл или текст, отправленный пользователем, и отправляет результат анализа.
    """
    file_info = await message.document.get_file() if message.document else None
    code = message.text if not file_info else None

    # Если это файл, скачиваем его
    if file_info:
        downloaded_file = await message.bot.download_file(file_info.file_path)
        # Преобразуем содержимое файла в строку (например, для Python файла)
        code = downloaded_file.decode('utf-8')  # Предполагаем, что это текстовый файл

    if code:
        # Отправляем код на анализ
        analysis_result = analyze_code_with_model(code)
        
        # Формируем ответ с помощью format_response
        formatted_response = format_response(analysis_result)
        
        # Отправляем отформатированный результат пользователю
        await message.answer(formatted_response)
    else:
        await message.answer("Не удалось получить код для анализа.")
