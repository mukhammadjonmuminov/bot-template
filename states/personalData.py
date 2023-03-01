from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    full_name = State()
    email = State()
    phone_number = State()