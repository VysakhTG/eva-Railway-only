from datetime import datetime

from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message 

@Client.on_message(filters.command("bug"))
async def bug(bot, message):
    if msg.chat.username:
        chat_username = f"@{message.chat.username}/`{message.chat.id}`"
    else:
        chat_username = f"ᴩʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴩ/`{msg.chat.id}`"
    bugs = content(msg)
    user_id = message.from_user.id
    if bugs:
            await message.reply_text(
                f"<b>ʙᴜɢ ʀᴇᴩᴏʀᴛ : </b>\n\n"
                "<b>» ʙᴜɢ sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴩᴏʀᴛᴇᴅ ᴀᴛ sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ !</b>",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data=f"close_reply")]]
                ),
            )
    await client.send_message(LOG_CHANNEL, script.LOG_TEXT_B.format(bugs, message.from_user.mention, message.from_user.id))
@Client.on_callback_query(filters.regex("close_reply"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()

