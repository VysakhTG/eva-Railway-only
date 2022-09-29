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
