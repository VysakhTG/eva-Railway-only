from datetime import datetime

from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message 

@Client.on_message(filters.command("bug"))
async def bug(bot, message):
