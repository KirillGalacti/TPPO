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
    id = message.from_user.id
    with open('users_test_one.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for i in data:
            if int(i) == id:
                user = False
                break
            else:
                user = True
    if user:
        await message.answer("Описание опросника")
        await message.answer('Вопрос №1\nСколько вам лет?\nНапишите ответ (только число)', reply_markup=ReplyKeyboardRemove())
        await CallbackOnStart.Q1.set()
    else:
        await message.answer(text="Вы уже проходили тест")

@dp.message_handler(state=CallbackOnStart.Q1)
async def affairs(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(age=answer)
    await message.answer(text="Вопрос №2\nКак ваши дела?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q2.set()

@dp.message_handler(state=CallbackOnStart.Q2)
async def work(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(affairs=answer)
    await message.answer(text="Вопрос №3\nГде учитесь/работаете?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q3.set()

@dp.message_handler(state=CallbackOnStart.Q3)
async def season(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(work=answer)
    await message.answer(text="Вопрос №4\nКакое у вас время года?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q4.set()

@dp.message_handler(state=CallbackOnStart.Q4)
async def weather(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(season=answer)
    await message.answer(text="Вопрос №5\nКакая у вас погода?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q5.set()

@dp.message_handler(state=CallbackOnStart.Q5)
async def game(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(weather=answer)
    await message.answer(text="Вопрос №6\nЛюбите ли вы играть в компьютерные игры?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q6.set()

@dp.message_handler(state=CallbackOnStart.Q6)
async def country(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(game=answer)
    await message.answer(text="Вопрос №7\nВ какой стране вы находитесь?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q7.set()

@dp.message_handler(state=CallbackOnStart.Q7)
async def eat(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(country=answer)
    await message.answer(text="Вопрос №8\nКакое ваше любимое блюдо?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q8.set()

@dp.message_handler(state=CallbackOnStart.Q8)
async def sport(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(eat=answer)
    await message.answer(text="Вопрос №9\nКакой ваш любимый вид спорта?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q9.set()

@dp.message_handler(state=CallbackOnStart.Q9)
async def hobby_sport(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(sport=answer)
    await message.answer(text="Вопрос №10\nУвлекаетесь ли спортом?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q10.set()

@dp.message_handler(state=CallbackOnStart.Q10)
async def tv(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(hobby_sport=answer)
    await message.answer(text="Вопрос №11\nЛюбите ли вы смотреть телевизор?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q11.set()

@dp.message_handler(state=CallbackOnStart.Q11)
async def walk(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(tv=answer)
    await message.answer(text="Вопрос №12\nВы любите гулять?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q12.set()

@dp.message_handler(state=CallbackOnStart.Q12)
async def clothes(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(walk=answer)
    await message.answer(text="Вопрос №13\nКакой ваш любимы элемент одежды?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q13.set()

@dp.message_handler(state=CallbackOnStart.Q13)
async def shoes(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(clothes=answer)
    await message.answer(text="Вопрос №14\nКакой ваш любимы элемент обуви?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q14.set()

@dp.message_handler(state=CallbackOnStart.Q14)
async def bedtime(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(shoes=answer)
    await message.answer(text="Вопрос №15\nВо сколько вы ложитесь спать?\nОтвет дать числом.",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q15.set()

@dp.message_handler(state=CallbackOnStart.Q15)
async def sleep_time(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(bedtime=answer)
    await message.answer(text="Вопрос №16\nСколько вы спите в день?\nОтвет дать числом.",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q16.set()

@dp.message_handler(state=CallbackOnStart.Q16)
async def get_up(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(sleep_time=answer)
    await message.answer(text="Вопрос №17\nВо сколько вы обычно просыпаетесь?\n Ответ дать числом.",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q17.set()

@dp.message_handler(state=CallbackOnStart.Q17)
async def health(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(get_up=answer)
    await message.answer(text="Вопрос №18\nВы хорошо следите за своим здоровьем?",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q18.set()

@dp.message_handler(state=CallbackOnStart.Q18)
async def trip(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(health=answer)
    await message.answer(text="Вопрос №19\nВы собираетесь куда-то поехать в ближайшее время?\nЕсли да, то напишите куда.",
                         reply_markup=ReplyKeyboardRemove())
    await CallbackOnStart.Q19.set()

@dp.message_handler(state=CallbackOnStart.Q19)
async def tower(message: types.Message, state: FSMContext):
    b = towers()
    answer = message.text
    await state.update_data(trip=answer)
    await message.answer(text="Вопрос №20\nВ каком городе вы живете сейчас?\nВыберите ответ из предложенных",
                         reply_markup=b)
    await CallbackOnStart.next()


@dp.callback_query_handler(state=CallbackOnStart.Q20)
async def end(call: types.Message, state: FSMContext):
    answer = call.data
    await state.update_data(full_name=call.from_user.full_name)
    await state.update_data(city=answer)
    data = await state.get_data()
    user = {call.from_user.id: data}
    text = []
    for i in data:
        text.append(f'{data[i]}\n')
    await call.message.answer(text="Спасибо за прохождения опросника!\nВсе ваши ответы были записаны в документ формата JSON.", reply_markup=ReplyKeyboardRemove())
    # await call.message.answer('\n'.join(text))
    with open('users_test_one.json', encoding='utf-8') as file:
        data = json.load(file)
        data.update(user)
        with open('users_test_one.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
    await state.finish()

