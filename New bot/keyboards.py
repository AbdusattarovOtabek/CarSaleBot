from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

contact_btn = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='📞 Telefon raqam', request_contact=True),
    ]
], 
    resize_keyboard=True,
)

lang_btn = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🇺🇿 Uzbek"), 
        KeyboardButton(text="🇷🇺 Rus"),
        KeyboardButton(text="🇬🇧 Ingliz")
    ]
], 
    resize_keyboard=True,
)

handle_role = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Sotuvchi"),
        KeyboardButton(text="Haridor")
    ]
],
    resize_keyboard=True
)