from info import CAPTION 
from pyrogram import Client, filters

async def get_size(size):
    p=size/1048597           #size in MB
    if p>1024:
         c=round(p/1024, 2)
         filezize=f"{c} GB"
    elif p>1:
         c=round(p, 2)
         filezize=f"{c} MB"
    else:
         c=round(size/1024, 1)
         filezize=f"{c} KB"
    return filezize

async def get_caption(name):
    if "_" in name:
        newcap=name.replace("_", " ")     
    else:
        newcap=name
    return newcap 

def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@Client.on_message(filters.private & filters.command("caption"))
async def start(bot, message): 
    caption = content(message)
    await message.reply(f"Hello {message.from_user.mention},\nI will edit channel message's captions.\nAdd me to your channel with necessary permissions.")

@Client.on_message(filters.channel & filters.document) #add more filters if you want.
async def caption(bot, message):
   try:
       await message.edit(caption(name=await get_caption(message.document.file_name),    
                                         size=await get_size(message.document.file_size))
                          )
   except Exception as e:
       print(e)
