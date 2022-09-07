from pyrogram import Client, filters 
from pyrogram.types import Message  
import asyncio
import time 
import os 
from info import ADMINS 

@Client.on_message(filters.private & filters.command(["forward"]))
async def forward(client, message): 
    msg = await client.send_message(chat_id=query.message.chat.id, text="<b>❪ SET TARGET CHAT ❫\n\nForward a message from Your target chat</b>")
    t_chat = message.forward_from_chat
    msg1 = await bot.ask(chat_id=query.message.chat.id, text="<b>Send Starting Message From Where you want to Start forwarding</b>")
    msg2 = await bot.ask(chat_id=query.message.chat.id, text="<b>Send Ending Message from same cha</b>")
    # print(msg1.forward_from_message_id, msg1.forward_from_chat.id, msg1.forward_from_message_id) 
    i_chat = msg1.forward_from_chat
    s_msg = int(msg1.forward_from_message_id)
    f_msg = int(msg2.forward_from_message_id)+1 
    await message.reply_text('**Forwarding Started**\n\nPress /restart to Stop and /log to get log TXT file') 
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
