from pyrogram import Client, filters 
from pyrogram.types import Message, User, ChatJoinRequest
@Client.on_chat_join_request((filters.group | filters.channel))
async def autoapprove(bot: Client, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    await bot.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
