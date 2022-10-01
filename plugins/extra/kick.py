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
    action = banbot.send_message(chat_id=chat, text="`Processing… ⏳`")
    await action.edit(Text.PROCESSING.format("⏳", "⏳", text, 0, 0, 0))
    async for member in banbot.get_chat_members(self=pyrogram.Client, chat_id=chat):
        memberslist.append(member)
        await action.edit(Text.PROCESSING.format(len(memberslist) + " members found", "⏳", text, 0, 0, 0))
    memberscount = len(memberslist)
    adminscount = len(adminlist)
    for member in range(memberscount):
        if memberslist[member] in adminlist:
            memberslist.pop(member)
    actioncount = memberscount - adminscount
    donecount = 0
    errorcount = 0
    errorlist = []
    await action.edit(Text.PROCESSING.format(memberscount + " members found", "Done ✅", text, donecount, actioncount, errorcount))
    for member in range(actioncount):
        try:
            useraction = memberslist[member].user.id
            if mode == 0:
                await banbot.ban_chat_member(chat_id=chat, user_id=useraction, until_date=datetime.now() + timedelta(seconds=31))
            elif mode == 1:
                await banbot.ban_chat_member(chat_id=chat, user_id=useraction)
            donecount+=1
        except FloodWait as f:
            await sleep(f.x)
            member-=1
        except Exception as e:
            LOGGER.warning(e)
            donecount+=1
            errorcount+=1
            errrorlist.append(useraction)
        await action.edit(Text.PROCESSING.format(memberscount + " members found", "Done ✅", text, donecount, actioncount, errorcount))
    if len(errorlist) > 0:
        errorfile = open(f"errors_{chat}.txt", "w")
        for item in errorlist:
            errorfile.write(item + "\n")
        errorfile.close()
        with open(f"errors_{chat}.txt", "rb") as doc_f:
            try:
                await banbot.send_document(
                    chat_id=chat,
                    document=doc_f,
                    file_name=doc_f.name
                )
                LOGGER.info(f"Log file sent to {chat}")
            except FloodWait as e:
                await sleep(e.x)
            except RPCError as e:
                message.reply_text(e, quote=True)
                LOGGER.warn(f"Error in /log : {e}")
        return await action.edit(f"Done ✅\nBanned {donecount} users, with {errorcount} errors. Check the file above to know which User ID's we failed to process")
    return await action.edit(f"Done ✅\nBanned {donecount} users")

@Client.on_message(filters.command("fusrodah")) # & filters.group
async def being_devil(_, message: Message):
    await message.reply("Confirm your action bro\nChoose either :\n• Kick all members except the admins\n• **Ban** all members except the admins\n• Cancel your task", reply_markup=Buttons.CONFIRMATION)
