# import json

# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
# from aiogram.types import ReplyKeyboardRemove

# from keyboards.inline.choice_but_start_test import towers

# from loader import dp
# from aiogram import types
# from states import CallbackOnStart


# @dp.message_handler(Command('onstarttest'))
# async def on_start_test(message: types.Message):
#     await message.answer("Описание опросника")
#     await message.answer('Вопрос №1\nСколько вам лет?\nНапишите ответ (только число)', reply_markup=ReplyKeyboardRemove())
#     await CallbackOnStart.Q1.set()

# @dp.message_handler(state=CallbackOnStart.Q1)
# async def tower(message: types.Message, state: FSMContext):
#     answer = message.text
#     await state.update_data(age=answer)
#     await message.answer(text="как ваше настроение?", reply_markup=ReplyKeyboardRemove())
#     await CallbackOnStart.Q2.set()

# @dp.message_handler(state=CallbackOnStart.Q3)
# async def sun(message: types.Message, state: FSMContext):
#     answer = message.text
#     await state.update_data(sun=answer)
#     await message.answer('Вопрос №3\nКак ваше настроение?\n', reply_markup=ReplyKeyboardRemove())
#     await CallbackOnStart.next()


# @dp.callback_query_handler(state=CallbackOnStart.Q4)
# async def end(call: types.Message, state: FSMContext):
#     answer = call.data
#     await state.update_data(full_name=call.from_user.full_name)
#     await state.update_data(repost=answer)
#     data = await state.get_data()
#     user = {call.from_user.id: data}
#     text = []
#     for i in data:
#         text.append(f'{data[i]}\n')
#     await call.message.answer(text="Ваши ответы:", reply_markup=ReplyKeyboardRemove())
#     await call.message.answer('\n'.join(text))
#     with open('users_test_one.json', encoding='utf-8') as file:
#         data = json.load(file)
#         data.update(user)
#         with open('users_test_one.json', 'w', encoding='utf-8') as outfile:
#             json.dump(data, outfile, indent=4, ensure_ascii=False)
#     await state.finish()


import json

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline.choice_but_start_test import towers

from loader import dp
from aiogram import types
from states import CallbackOnStart


@dp.message_handler(Command('onstarttest'))
async def on_start_test(message: types.Message):
    await message.answer("Описание опросника")
    await message.answer('Вопрос №1\nСколько вам лет?\nНапишите ответ (только число)', reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q1.set()

@dp.message_handler(state=CallbackOnStart.Q1)
async def tower(message: types.Message, state: FSMContext):
    b = towers()
    answer = message.text
    await state.update_data(age=answer)
    await message.answer(text="Вопрос №2\nВ каком городе вы живете?\nВыберите ответ из предложенных",
                         reply_markup=b)
    await CallbackOnStart.Q2.set()


@dp.callback_query_handler(state=CallbackOnStart.Q2)
async def end(call: types.Message, state: FSMContext):
    answer = call.data
    await state.update_data(full_name=call.from_user.full_name)
    await state.update_data(repost=answer)
    data = await state.get_data()
    user = {call.from_user.id: data}
    text = []
    for i in data:
        text.append(f'{data[i]}\n')
    await call.message.answer(text="Ваши ответы:", reply_markup=ReplyKeyboardRemove())
    await call.message.answer('\n'.join(text))
    with open('users_test_one.json', encoding='utf-8') as file:
        data = json.load(file)
        data.update(user)
        with open('users_test_one.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
    await state.finish()

