from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import os 

TOKEN=os.environ['TOKEN']
from flask import Flask, request


app=Flask(__name__)

@app.route('/')


def start(update: Update, context:CallbackContext):
    chat_id=update.message.chat.id 
    keyboar=ReplyKeyboardMarkup([
        ['Uzbek tili'],['русский язык']
    ])
    bot=context.bot
    bot.sendMessage(chat_id=chat_id, text='Tilni tanlang // Выберите язык',reply_markup=keyboar)
def malumot(update: Update, context:CallbackContext):
    chat_id=update.message.chat.id
    keyboar=ReplyKeyboardMarkup([
        ["Ma'lumot olish", "Biz bilan bog'lanish"]
    ])
    bot=context.bot
    bot.sendMessage(chat_id=chat_id,text="Assalomu alaykum xurmatli mijoz siz bu bot orqali uzingizni qiziqtirgan savollarga javob topishingiz hamda mahsulot xarid qilish uchun biz bilan bog'lanishingiz mumkin", reply_markup=keyboar)

if __name__ =='__main__':
    app.run()
updater=Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Uzbek tili'),malumot))
updater.start_polling()
updater.idle()

