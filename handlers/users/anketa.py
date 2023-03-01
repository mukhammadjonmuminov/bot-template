from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData

@dp.message_handler(Command("anketa"))
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting\n"
                         "/help")
    await PersonalData.full_name.set()

@dp.message_handler(state=PersonalData.full_name)
async def answer_fullname(message: types.Message, state: FSMContext):
    full_name = message.text
    # await state.update_data(name=full_name)
    await state.update_data(
        {"full_name": full_name}
    )
    await message.answer("Email manzil kiriting")
    await PersonalData.next()
    # await PersonalData.email.set()

@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    await state.update_data(
        {"email": email}
    )
    await message.answer("Telefon raqam kiriting:")
    await PersonalData.next()

@dp.message_handler(state=PersonalData.phone_number)
async def answer_phoneNumber(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(
        {
            "phone_number": phone_number
        }
    )

    # Ma'lumotlarni qayta o'qiymiz
    data = await state.get_data()
    full_name = data.get("full_name")
    email = data.get("email")
    phone_number = data.get("phone_number")
    await message.answer(f"Quyidagi ma'lumotlar qabul qilindi\n"
                         f"Ism: {full_name}\n"
                         f"Email: {email}\n"
                         f"Phone number: {phone_number}")
    await state.finish()
    # await state.reset_state(with_data=False)
