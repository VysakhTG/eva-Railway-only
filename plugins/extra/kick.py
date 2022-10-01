import os
import logging
from asyncio import sleep 
import pyrogram
from datetime import datetime, timedelta
from pyrogram import Client, enums, filters, idle
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
@Client.on_callback_query(filters.regex(r'^kick'))
def NewChat(bot, query):
    cid=query.chat.id
    logging.info("new chat {}".format(cid))
    logging.info("getting memebers from {}".format(cid))
    a= bot.iter_chat_members(cid)
    for i in a:
        try:
            bot.kick_chat_member(chat_id=cid,user_id=i.user.id)
            logging.info("kicked {} from {}".format(i.user.id,cid))
        except Exception:
            logging.info(" failed to kicked {} from {}".format(i.user.id,cid))
            
    logging.info("process completed")
