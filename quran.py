from telegram import *
from telegram.ext import *
# from requests import *

print("Bot started...")

def start_command(update,context):
    text="Salom! "
    text+=update.message.chat.first_name
    text+=" "
    text+=update.message.chat.last_name
    text+="\nBuyruqlar:\n/about - Qur'on haqida\n/help - Yordam"
    buttons=[
        [
            InlineKeyboardButton("Al-Faatiha (سُورَةُ ٱلْفَاتِحَةِ)", callback_data="1"),
            InlineKeyboardButton("Al-Baqara (سُورَةُ البَقَرَةِ)", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]
    update.message.reply_text(text)
    update.message.reply_text("",reply_markup=InlineKeyboardMarkup(buttons))

def about_command(update,context):
    update.message.reply_text("Qur'on")

def help_command(update,context):
    update.message.reply_text("Buyruqlar:\n/about - Qur'on haqida\nMurojaat uchun: @aziz2004official")

def error(update,context):
    print(f"Yangilash: {update} Xatolik: {context.error}")

def main():
    updater=Updater("5480920558:AAHkXEPFFrDIObibLhocMNCeXOLLmwsDo7c",use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("about",about_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()