from pyrogram import Client, filters 
from pyrogram.types import Message, User, ChatJoinRequest

TEXT =  "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")


@Client.on_chat_join_request((filters.group | filters.channel))
async def autoapprove(bot: Client, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))
