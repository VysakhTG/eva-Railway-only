from pyrogram import Client, filters 
from pyrogram.types import Message  
import asyncio
import time 
import os 
from info import ADMINS 

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def forward(bot, message): 
    to_channel = 
    from_channel =
    start_skip =
    end_skip =
    await message.reply_text('**Forwarding Started**')
    try:
        for i in range(s_msg, f_msg):
            try:
                await bot.copy_message(
                    chat_id= t_chat,
                    from_chat_id= i_chat,
                    message_id= i
                )
                time.sleep(2)
            except Exception:
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done Forwarding")
