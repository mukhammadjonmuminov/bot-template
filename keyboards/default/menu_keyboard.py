from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
speciality = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Intensive Kurslar"),
        ],
        [
            KeyboardButton(text="Mutaxasislik Kurslar"),
        ],
        [
            KeyboardButton(text="Bootcamp Kurslar"),
        ]
    ],
    resize_keyboard=True
)

