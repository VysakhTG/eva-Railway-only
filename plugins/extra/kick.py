import os
import logging
from asyncio import sleep 
import pyrogram
from datetime import datetime, timedelta
from pyrogram import Client, enums, filters
from pyrogram.types import BotCommand, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait, RPCError

LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARN)

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('logs.txt'), logging.StreamHandler()],
    format="%(asctime)s - %(levelname)s - %(name)s - %(threadName)s - %(message)s"
)

class Buttons:
    CONFIRMATION = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Kick 🚪", callback_data="kick"),
                InlineKeyboardButton("Ban 🕳", callback_data="ban")
            ],
            [
                InlineKeyboardButton("Cancel ❌", callback_data="nope")
            ]
        ])

class Text:
    PROCESSING = """
Retrieving members of the chat… {}
Comparing with the admins of the chat… {}
{} members… {}/{} ({} errors)
    """
@Client.on_callback_query()
async def callbacks(banbot: Client, query: CallbackQuery):
    cid = query.message.chat.id
    uid = query.from_user.id
    qid = query.message.id
    if query.data == "nope":
        return await query.edit_message_text("❌ Successfully canceled your task ✅")
    elif query.data == "kick":
        await justdoit("Kicking", 0, cid, uid, qid)
    elif query.data == "ban":
        await justdoit("Banning", 1, cid, uid, qid) 

async def justdoit(text, mode, chat, user, query):
    await Client.delete_messages(chat_id=chat, message_ids=query)
    memberslist = []
    await banbot.ban_chat_member(chat_id=chat, user_id=useraction, until_date=datetime.now() + timedelta(seconds=31))
            
