from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot_template.keyboards.default.start import menuStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("Telefoningiz va manzilingizni kiriting", reply_markup=menuStart)
