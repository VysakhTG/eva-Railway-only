from pyrogram import Client,filters 
from info import SUPPORT_CHAT

@Client.on_message(filters.command("bg")) 
async def bg(bot, message): 
    bugs = content(msg)
        await client.send_message(LOG_CHANNEL,(bugs))
