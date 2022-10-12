import requests
import logging
from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message 



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

@Client.on_message(filters.command("torrent"))
def torr_serch(update: Update, context: CallbackContext) -> None:
    q = content(message)
    try:
        update.message.reply_text("Searching results for {}".format(update.message.text))
        url = "https://api.sumanjay.cf/torrent/?query={}".format(update.message.text)
        results = requests.get(url).json()
        print(results)
        for item in results:
            age = item.get('age')
            leech = item.get('leecher')
            mag = item.get('magnet')
            name = item.get('name')
            seed = item.get('seeder')
            size = item.get('size')
            typ= item.get('type')
            update.message.reply_text(f"""*Name:* {name}
_Uploaded {age} ago_
*Seeders:* `{seed}`
*Leechers:* `{leech}`
*Size:* `{size}`
*Type:* {typ}
*Magnet Link:* `{mag}`""", parse_mode=ParseMode.MARKDOWN)
        update.message.reply_text("End of the search results...")
    except:
        update.message.reply_text("""Search results completed...
If you've not seen any results, try researching...!""")
