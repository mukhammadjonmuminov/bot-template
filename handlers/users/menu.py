from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu_keyboard, menuList_keyboard

from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Yo'nalishlardan birini tanglang:", reply_markup=menu_keyboard.speciality)

@dp.message_handler(text="Intensive Kurslar")
async def intensive_click(message: Message):
    await message.answer("Intensive Kurslar", reply_markup=menuList_keyboard.intensiveMenu)

@dp.message_handler(text="Mutaxasislik Kurslar")
async def intensive_click(message: Message):
    await message.answer("Mutaxasislik Kurslar", reply_markup=menuList_keyboard.specialityMenu)

@dp.message_handler(text="Bootcamp Kurslar")
async def intensive_click(message: Message):
    await message.answer("Bootcamp Kurslar", reply_markup=menuList_keyboard.bootcampMenu)

@dp.message_handler(text="⬅️ Ortga")
async def click_python(message: Message):
    await message.answer("Yo'nalishlardan birini tanglang:", reply_markup=menu_keyboard.speciality)


@dp.message_handler(text="🏘 Boshiga")
async def click_python(message: Message):
    await message.answer("Yo'nalishlardan birini tanglang:", reply_markup=menu_keyboard.speciality)

# @dp.message_handler(text="Python")
# async def click_python(message: Message):
#     await message.answer("Python darslari", reply_markup=python_keyboard.menuPython)
#
# @dp.message_handler(text="#00 Kirish")
# async def send_link(message: Message):
#     await message.answer("pipsudo.uz", reply_markup=ReplyKeyboardRemove())
#
# @dp.message_handler(text="🏘 Boshiga")
# async def click_python(message: Message):
#     await message.answer("Kurslarni tanglang", reply_markup=menu_keyboard.menu)