from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from bot_template.keyboards.default import menu_keyboard, python_keyboard

from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Kurslarni tanglang", reply_markup=menu_keyboard.menu)

@dp.message_handler(text="Telegram bot")
async def send_link(message: Message):
    await message.answer("Mukammal Telegram bot kursi: https://you.com")

@dp.message_handler(text="Python")
async def click_python(message: Message):
    await message.answer("Python darslari", reply_markup=python_keyboard.menuPython)

@dp.message_handler(text="#00 Kirish")
async def send_link(message: Message):
    await message.answer("pipsudo.uz", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="🏘 Boshiga")
async def click_python(message: Message):
    await message.answer("Kurslarni tanglang", reply_markup=menu_keyboard.menu)