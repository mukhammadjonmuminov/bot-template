from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from bot_template.states.personalData import PersonalData

from loader import dp

@dp.message_handler(CommandHelp(), state=PersonalData.full_name)
async def bot_help(message: types.Message):
    text = ("Iltimos ism va familyangizni quyidagi ko'rinishda kiriting: \nMustafo Muminov")

    await message.answer(text)

@dp.message_handler(CommandHelp(), state=None)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))