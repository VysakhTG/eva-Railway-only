from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram.enums import MessageMediaType
from pyrogram import Client, filters
import os 
import humanize
from PIL import Image
import time
from asyncio import sleep

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 𝚂𝚃𝙰𝚁𝚃 𝚁𝙴𝙽𝙰𝙼𝙴 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass
@Client.on_callback_query(filters.regex('cancel'))
async def cancel(bot,update):
	try:
           await update.message.delete()
	except:
           return

@Client.on_callback_query(filters.regex('rename'))
async def rename(bot,update):
	user_id = update.message.chat.id
	date = update.message.date
	await update.message.delete()
	await update.message.reply_text("__𝙿𝚕𝚎𝚊𝚜𝚎 𝙴𝚗𝚝𝚎𝚛 𝙽𝚎𝚠 𝙵𝚒𝚕𝚎𝙽𝚊𝚖𝚎...__",	
	reply_to_message_id=update.message.reply_to_message.id,  
	reply_markup=ForceReply(True))

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    reply_message = message.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
       new_name = message.text 
       await message.delete() 
       msg = await client.get_messages(message.chat.id, reply_message.id)
       file = msg.reply_to_message
       media_type = file.media.value
       media = getattr(file, media_type)
       if not "." in new_name:
          if "." in media.file_name:
              extn = media.file_name.rsplit('.', 1)[-1]
          else:
              extn = "mkv"
          new_name = new_name + "." + extn
       await reply_message.delete()
       button = [[InlineKeyboardButton("📁 𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃𝚂",callback_data = "upload_document")]]
       if media_type in [MessageMediaType.VIDEO, MessageMediaType.DOCUMENT]:
           button.append([InlineKeyboardButton("🎥 𝚅𝙸𝙳𝙴𝙾",callback_data = "upload_video")])
       elif media_type == MessageMediaType.AUDIO:
           button.append([InlineKeyboardButton("🎵 𝙰𝙾𝚄𝙳𝙸𝙾",callback_data = "upload_audio")])
       await message.reply_text(
          f"**Select the output file type**\n**Output FileName** :-```{new_name}```",
          reply_to_message_id=file.id,
          reply_markup=InlineKeyboardMarkup(button))

@Client.on_callback_query(filters.regex("upload"))
async def doc(bot,update):
     type = update.data.split("_")[1]
     new_name = update.message.text
     new_filename = new_name.split(":-")[1]
     file_path = f"downloads/{new_filename}"
     file = update.message.reply_to_message
     ms = await update.message.edit("𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳...")
     c_time = time.time()
     try:
     	path = await bot.download_media(message = file, progress=progress_for_pyrogram,progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳....",  ms, c_time   ))
     except Exception as e:
     	await ms.edit(e)
     	return 
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     duration = 0
     try:
        metadata = extractMetadata(createParser(file_path))
        if metadata.has("duration"):
           duration = metadata.get('duration').seconds
     except:
        pass
     user_id = int(update.message.chat.id) 
     ph_path = None 
     media = getattr(file, file.media.value)
     c_caption = await db.get_caption(update.message.chat.id)
     c_thumb = await db.get_thumbnail(update.message.chat.id)
     if c_caption:
         caption = c_caption.format(filename=new_filename, filesize=humanize.naturalsize(media.file_size), duration=convert(duration))
     else:
         caption = f"**{new_filename}**"
     if (media.thumbs or c_thumb):
         if c_thumb:
            ph_path = await bot.download_media(c_thumb) 
         else:
            ph_path = await bot.download_media(media.thumbs[0].file_id)
         Image.open(ph_path).convert("RGB").save(ph_path)
         img = Image.open(ph_path)
         img.resize((320, 320))
         img.save(ph_path, "JPEG")
     await ms.edit("𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶....")
     c_time = time.time() 
     try:
        if type == "document":
           await bot.send_document(
		    update.message.chat.id,
                    document=file_path,
                    thumb=ph_path, 
                    caption=caption, 
                    progress=progress_for_pyrogram,
                    progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶....",  ms, c_time   ))
        elif type == "video": 
            await bot.send_video(
		    update.message.chat.id,
		    video=file_path,
		    caption=caption,
		    thumb=ph_path,
		    duration=duration,
		    progress=progress_for_pyrogram,
		    progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶....",  ms, c_time))
        elif type == "audio": 
            await bot.send_audio(
		    update.message.chat.id,
		    audio=file_path,
		    caption=caption,
		    thumb=ph_path,
		    duration=duration,
		    progress=progress_for_pyrogram,
		    progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶....",  ms, c_time   )) 
     except Exception as e: 
         await ms.edit(e) 
         os.remove(file_path)
         if ph_path:
           os.remove(ph_path)
     await ms.delete() 
     os.remove(file_path) 
     if ph_path:
        os.remove(ph_path) 
