from pyrogram import Client, filters 
from pyrogram.types import Message  
import asyncio
import time 
import os 
from info import ADMINS 

TO_CHANNEL = -1737494519
FROM_CHANNEL = -1752475005
START_M = 4
END_M = 2000
 
@Client.on_message(filters.command("forward") & filters.user(ADMINS))
async def forward(bot, message): 
    await message.reply_text('**Forwarding Started**\n\nPress /restart to Stop and /log to get log TXT file')
    try:
        for i in range(START_M, END_M):
            try:
                await bot.copy_message(
                    chat_id= TO_CHANNEL,
                    from_chat_id= FROM_CHANNEL,
                    message_id= i,
                    caption=Config.CAPTION
                )
                time.sleep(2)
            except Exception:
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done Forwarding")
