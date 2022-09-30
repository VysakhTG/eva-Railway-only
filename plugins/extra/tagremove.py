import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

@Client.on_message(filters.channel & filters.forwarded)
async def fwdrmv(c, m):
    try:
        if m.media and not (m.video_note or m.sticker):
            await m.copy(m.chat.id, caption = m.caption if m.caption else None)
            await m.delete()
        else:
            await m.copy(m.chat.id)
            await m.delete()
    except FloodWait as e:
        await asyncio.sleep(e.x)
