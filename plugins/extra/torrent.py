import os
import aiohttp
import json
from pyrogram import Client, filters, emoji
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


m = None
i = 0
a = None
query = None


@Client.on_message(filters.command(["torrent"]))
async def torrent(_, message):
    global m
    global i
    global a
    global query
    try:
        await message.delete()
    except:
        pass
    if len(message.command) < 2:
        await message.reply_text("/torrent ᴀɴᴅ ᴛʏᴘᴇ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ")
        return
    query = message.text.split(None, 1)[1].replace(" ", "%20")
    m = await message.reply_text("Searching\nThis might take a while")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://itor.api-zero.workers.dev/?name={query}") \
                    as resp:
                a = json.loads(await resp.text())
    except:
        await m.edit("Found Nothing.")
        return
    result = (
        f"**Page - {i+1}**\n\n"
        f"➲Name: {a[i]['name']}\n"
        f"➲Link: `{a[i]['link']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Next",
                                         callback_data="next"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="delete")
                ]
            ]
        ),
        parse_mode="markdown",
    )


@Client.on_callback_query(filters.regex("next"))
async def callback_query_next(_, message):
    global i
    global m
    global a
    global query
    i += 1
    result = (
        f"**Page - {i+1}**\n\n"
        f"➲Name: {a[i]['name']}\n"
        f"➲Link: `{a[i]['link']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Back",
                                         callback_data="back"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="delete"),
                    InlineKeyboardButton(f"Next",
                                         callback_data="next")
                    
                ]
            ]
        ),
        parse_mode="markdown",
    )


@Client.on_callback_query(filters.regex("back"))
async def callback_query_previous(_, message):
    global i
    global m
    global a
    global query
    i -= 1
    result = (
        f"**Page - {i+1}**\n\n"
        f"➲Name: {a[i]['name']}\n"
        f"➲Link: `{a[i]['link']}`\n\n\n"
    )
    await m.edit(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Back",
                                         callback_data="back"),
                    InlineKeyboardButton(f"{emoji.CROSS_MARK}",
                                         callback_data="delete"),
                    InlineKeyboardButton(f"Next",
                                         callback_data="next")
                ]
            ]
        ),
        parse_mode="markdown",
    )


@Client.on_callback_query(filters.regex("delete"))
async def callback_query_delete(_, message):
    global m
    global i
    global a
    global query
    await m.delete()
    m = None
    i = 0
    a = None
    query = None

__help__ = """
 - /torrent <movie name>: Get Your Torrent Link From Various Resource. 
"""

__mod_name__ = "Torrent"
