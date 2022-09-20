from pyrogram import filters, Client
from pyrogram.types import Message 

def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    
@Client.on_message(filters.command("tagall")) 
async def tagall(client, message):
    await message.reply("`Processing.....`")
    sh = content(message)
    if not sh:
        sh = "Hi!"
    mentions = ""
    async for member in Client.iter_chat_members(message.chat.id):
        mentions += member.user.mention + " "
    n = 4096
    kk = [mentions[i : i + n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"<b>{sh}</b> \n{i}"
        await client.send_message(message.chat.id, j, parse_mode="html")
