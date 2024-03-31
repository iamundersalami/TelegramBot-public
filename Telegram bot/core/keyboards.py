from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🎲 Dice 🎲'),
            KeyboardButton(text='🏀 Basketball 🏀'),
        ],
        [
            KeyboardButton(text='💰 Bitcoin 💰'),
            KeyboardButton(text='🔷 Etherium 🔷')
        ],
        [
            KeyboardButton(text='☀ Weather ☀')
        ],
        [
            KeyboardButton(text='🌐 Contacts 🌐')
        ]

    ],
    resize_keyboard=True,
    input_field_placeholder='Enter a command'
)


