import asyncio
from info import ADMINS
from os import environ
from pyrogram import Client, filters, idle

@Client.on_message(filters.command(["adelete"])) 
async def adelete(bot, message):
    try:
       if message.from_user.id not in ADMINS:
          return
       else:
          await asyncio.sleep(5)
          await bot.delete_messages(message.chat.id)
