err1 = "**__One subtitle is processing wait sometime__**"
err2 = "**__This is not a subtitle(srt) file__**"
err3 = "**Todays limit exceeded**"
err4 = "**Unsupported characters in file**"
err5 = "**Some errors happened Try again..**"

langs = [
    [
        InlineKeyboardButton("മലയാളം", callback_data="Malayalam"),
        InlineKeyboardButton("தமிழ்", callback_data="Tamil"),
        InlineKeyboardButton("हिन्दी", callback_data="Hindi"),
    ],
    [
        InlineKeyboardButton("ಕನ್ನಡ", callback_data="Kannada"),
        InlineKeyboardButton("తెలుగు", callback_data="Telugu"),
        InlineKeyboardButton("मराठी", callback_data="Marathi"),
    ],
    [
        InlineKeyboardButton("ગુજરાતી", callback_data="Gujarati"),
        InlineKeyboardButton("ଓଡ଼ିଆ", callback_data="Odia"),
        InlineKeyboardButton("বাংলা", callback_data="bn"),
    ],
    [
        InlineKeyboardButton("ਪੰਜਾਬੀ", callback_data="Punjabi"),
        InlineKeyboardButton("فارسی", callback_data="Persian"),
        InlineKeyboardButton("English", callback_data="English"),
    ],
    [
        InlineKeyboardButton("español", callback_data="Spanish"),
        InlineKeyboardButton("français", callback_data="French"),
        InlineKeyboardButton("русский", callback_data="Russian"),
    ],
    [
        InlineKeyboardButton("עִברִית", callback_data="hebrew"),
        InlineKeyboardButton("العربية", callback_data="arabic"),
        InlineKeyboardButton("සිංහල",callback_data="sinhala"),
    ],
]
