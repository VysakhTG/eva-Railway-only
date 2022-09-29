from pyrogram import Client, filters 
from pyrogram.types import Message  
import asyncio
import time 
import os 
from info import ADMINS 

@Client.on_message(filters.command("forward") & filters.user(ADMINS))
async def forward(bot, message): 
    to_channel = "-1737494519"
    from_channel = "-1752475005"
    start_skip = "1"
    end_skip = "516348"
    await message.reply_text('**Forwarding Started**')
    try:
        for i in range(start_skip, end_skip):
            try:
                await bot.copy_message(
                    chat_id= to_channel,
                    from_chat_id= from_channel,
                    message_id= i
                )
                time.sleep(2)
            except Exception:
                continue
    except Exception as e:
        await message.reply_text(str(e))
    await message.reply_text("Done Forwarding")
