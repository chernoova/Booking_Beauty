from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from functools import lru_cache


@lru_cache()
def keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Клиент", callback_data="client"),
                                                 InlineKeyboardButton(text="Салон", callback_data="saloon")]])