from pyrogram import Client, filters

api_id = 14406195
api_hash = "0e8c9f37d836042b5b2195ab79d68c76"
bot_token = "5568799979:AAHwIEf4vVBv40FxGa5f-9h4PceQD4hFy5g"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

@Client.on_message(filters.command("start"))
async def start_clone_bot(bot, message): 
    await app.send_message("**Process Cancelled Succefully !**")
        
