from telegram.ext import *
from datetime import datetime

print("Bot started...")

def start_command(update,context):
    text="Salom! "
    text+=update.message.chat.first_name
    text+=" "
    text+=update.message.chat.last_name
    text+="\n\n/song - Qo'shiq nomi bilan izlash\n\n/artist - Qo'shiqchi nomi bilan izlash\n\n/time - Vaqtni ko'rsatish\n\n/help - yordam"
    update.message.reply_text(text)
    
def song_commmand(update,context):
    update.message.reply_text("Qo'shiq nomini yozing")

def artist_command(update,context):
    update.message.reply_text("Qo'shiqchi nomini yozing")

def time_command(update,context):
    now=datetime.now()
    date_time=now.strftime("%d/%m/%Y, %H:%M:%S")
    date_time=str(date_time)
    update.message.reply_text(date_time)

def help_command(update,context):
    update.message.reply_text("Buyruqlar\n\n/song - Qo'shiq nomi bilan izlash\n\n/artist - Qo'shiqchi nomi bilan izlash\n\n/time - Vaqtni ko'rsatish\n\n/help - yordam\n\nBog'lanish uchun: @aziz2004official")

def error(update,context):
    print(f"Yangilash: {update} Xatolik: {context.error}")

def main():
    updater=Updater("5305921899:AAG8mf43-4sjzkKjZMGrtezbaNUWcsAUybo",use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("song",song_commmand))
    dp.add_handler(CommandHandler("artist",artist_command))
    dp.add_handler(CommandHandler("time",time_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()
