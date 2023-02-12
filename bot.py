from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import os 

TOKEN=os.environ['TOKEN']

def start(update: Update, context:CallbackContext):
    chat_id=update.message.chat.id 
    keyboar=ReplyKeyboardMarkup([
        ['Uzbek tili'],['русский язык']
    ])
    bot=context.bot
    bot.sendMessage(chat_id=chat_id, text='Tilni tanlang // Выберите язык',reply_markup=keyboar)



updater=Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()

