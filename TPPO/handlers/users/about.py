from aiogram import types
from aiogram.dispatcher.filters import Command


from loader import dp

@dp.message_handler(Command('about'))
async def about(message: types.Message):
    text = """Данный проект был выполнен в рамках индивидуального задания по дисциплине ТППО и не несет никакой смысловой нагрузки. Бот выполнен в стиле вопрос-ответ, ответы выгружаются в JSON-файл."""
    await message.answer(text=text)