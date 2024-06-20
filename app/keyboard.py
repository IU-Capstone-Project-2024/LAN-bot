from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

start = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Open web app',
                                                                    web_app=WebAppInfo(url='https://gmail.com'))]])

room = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Events', callback_data='Events')],
                                             [InlineKeyboardButton(text='Routine', callback_data='Routine')]
                                             ])
