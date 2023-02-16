from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import os 

TOKEN=os.environ['TOKEN']
#from flask import Flask, request


#app=Flask(__name__)

#@app.route('/')


def start(update: Update, context:CallbackContext):
    chat_id=update.message.chat.id 
    keyboar=ReplyKeyboardMarkup([
        ['Uzbek tili 🇺🇿'],['русский язык 🇷🇺']
    ])

    bot=context.bot
    bot.sendMessage(chat_id=chat_id, text='Tilni tanlang // Выберите язык',reply_markup=keyboar)
def uzbek_tili(update: Update, context:CallbackContext):
    chat_id=update.message.chat.id
    keyboar=ReplyKeyboardMarkup([
        ["Ma'lumot olish", "Biz bilan bog'lanish"], ["Asosiy menu"]
    ])
    bot=context.bot
    bot.sendMessage(chat_id=chat_id,text="Assalomu alaykum xurmatli mijoz siz bu bot orqali uzingizni qiziqtirgan savollarga javob topishingiz hamda mahsulot xarid qilish uchun biz bilan bog'lanishingiz mumkin", reply_markup=keyboar)

def aloqa(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    keyboar=InlineKeyboardMarkup([
        [InlineKeyboardButton(callback_data='tel',text='Telifon raqamimiz ☎️')],
        #[InlineKeyboardButton(url='tatamisooft.uz@gmail.com', text='Bizning email pochtamiz 📧')],
        [InlineKeyboardButton(text='Instagram profilimiz', url="https://instagram.com/sooft_uz?igshid=YmMyMTA2M2Y=")],
        [InlineKeyboardButton(text='Telegram kanalimiz', url='https://t.me/sooft_uz')],
        [InlineKeyboardButton(text='Locatsiyamiz', url='https://maps.app.goo.gl/qRtfHp1vHksMXUkx9')],
        [InlineKeyboardButton(text=' Bizning manzil', callback_data='manzilimiz')]
        
    ])
    bot.sendMessage(chat_id=chat_id, text="Marxamat tanlang!!!", reply_markup=keyboar)


def ruscha(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    keyboar=ReplyKeyboardMarkup([
        ['Получить информацию','связаться с нами'],['главное меню']
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboar, text='Здравствуйте, уважаемый покупатель, через этого бота вы можете найти ответы на интересующие вас вопросы и связаться с нами для приобретения продукции.')
def aloqa_ruscha(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    keyboar=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Наш номер телефона ☎️', callback_data='tel_ruscha')],
        [InlineKeyboardButton(text='Наш профиль в инстаграмм',url="https://instagram.com/sooft_uz?igshid=YmMyMTA2M2Y=")],
        [InlineKeyboardButton(text='Наш Telegram-канал', url='https://t.me/sooft_uz')],
        [InlineKeyboardButton(text='Наше место нахождения', url='https://maps.app.goo.gl/qRtfHp1vHksMXUkx9')],
        [InlineKeyboardButton(text='Наш адрес', callback_data='manzilimiz_ruscha')]


    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboar, text='Пожалуйста, выбери!!!')

def malumot_uzbekcha(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    keyboar=ReplyKeyboardMarkup([
        ['Rasmlari 📸'],['Ulchamlari va narxlari 💶'],['Orqaga qaytish ◀️']
    ])
    bot.sendMessage(chat_id=chat_id, text='Marxamat tanishib chiqishingiz mumkin!', reply_markup=keyboar)
def photo_uzbekcha(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo=open("photo_2022-10-20_09-35-37.jpg",'rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open("photo_2023-02-16_12-42-03.jpg",'rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open("photo_2023-02-16_12-42-10.jpg", 'rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open('photo_2023-02-16_13-55-33.jpg','rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open('photo_2023-02-16_13-55-48.jpg','rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open('photo_2023-02-16_13-56-04.jpg','rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open('photo_2023-02-16_13-56-28.jpg','rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open('photo_2023-02-16_13-56-37.jpg','rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open('photo_2022-10-28_16-01-18.jpg','rb'))
    #bot.sendMessage(chat_id=chat_id, text='Ulchamlari\n50sm*50sm\n60sm*60sm\n100sm*100sm\nNarxlari kvadratiga xisoblanadi\n1 sm qalinlikdagisi 70 000 sum\n2 sm qalinlikdagisi 130 000 sum\n4 sm qalinlikdagisi 260 000 sum\nTurli xil ranglaridan bor')
def money_uzbekcha(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    #bot.sendMessage(chat_id=chat_id, text='Ulchamlari\n50sm*50sm\n60sm*60sm\n100sm*100sm\nNarxlari kvadratiga xisoblanadi\n1 sm qalinlikdagisi 70 000 sum\n2 sm qalinlikdagisi 130 000 sum\n4 sm qalinlikdagisi 260 000 sum\nTurli xil ranglaridan bor')
    bot.sendPhoto(chat_id=chat_id, photo=open('Screenshot from 2023-02-16 17-08-03.png','rb'))
    bot.sendMessage(chat_id=chat_id, text='Sotib olmoqchi bulsangiz @sooft_admin akkauntiga olmoqchi bulgan maxsulotlaringizni ulchamlarini yozib yuboring uzimiz sizga aloqaga chiqamiz')

def money_ruscha(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo=open('Screenshot from 2023-02-16 17-39-44.png','rb'))
    bot.sendMessage(chat_id=chat_id, text='Если вы хотите купить, напишите размер продуктов, которые вы хотите купить, в аккаунт @sooft_admin, и мы свяжемся с вами.')





def malumot_ruscha(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    keyboar=ReplyKeyboardMarkup([
        ['картинки 📸'],['Размеры и цены 💶'],['возвращаться ◀️']
    ])
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboar, text='Взгляни, пожалуйста!')
   
    #bot.sendMessage(chat_id=chat_id, text='Размеры\n50см*50см\n60см*60см\n100см*100см\nЦена квадрата\n1 см толщина 70 000 сум\n2 см толщина 130 000 сум\n4 см толщина 260 000 сум\nРазличные цвета есть')
   
def photo_ruscha(update: Update, context: CallbackContext):
    chat_id=update.message.chat.id
    bot=context.bot
    bot.sendPhoto(chat_id=chat_id, photo=open("photo_2022-10-20_09-35-37.jpg",'rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open("photo_2023-02-16_12-42-03.jpg",'rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open("photo_2023-02-16_12-42-10.jpg", 'rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open('photo_2023-02-16_13-55-33.jpg','rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open('photo_2023-02-16_13-55-48.jpg','rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open('photo_2023-02-16_13-56-04.jpg','rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open('photo_2023-02-16_13-56-28.jpg','rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open('photo_2023-02-16_13-56-37.jpg','rb'))
    bot.sendPhoto(chat_id=chat_id, photo=open('photo_2022-10-28_16-01-18.jpg','rb'))




def query(update: Update, context: CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    data=query.data
    bot=context.bot
    
    

    if data=='tel':
       # bot.send_contact(chat_id=chat_id, phone_number="+998904776646", first_name='sooft_admin')
         bot.sendContact(chat_id=chat_id, phone_number=+998904776646, first_name='SOOFT_admin')
    elif data=='manzilimiz':
        bot.sendMessage(chat_id=chat_id, text="📍Bizning manzilimiz Samarqand viloyati Jomboy tumani Farhod shaharchasi Shirin mahallasida joylashgan.\n😎 Yana bir gap, bizga masofa hech qanday to'sqinlik qila olmaydi. Chunki Sooftda tezkor va ehtiyotlab yetkazib berish xizmati ham mavjud")
    elif data=='tel_ruscha':
        bot.sendContact(chat_id=chat_id, phone_number=+998904776646, first_name='SOOFT администратор')
    if data=='manzilimiz_ruscha':
        bot.sendMessage(chat_id=chat_id, text="📍Наш адрес находится в микрорайоне Ширин, г. Фарход, Жомбойский район, Самаркандская область.\n😎Потому что у Sooft также есть быстрая и точная служба доставки.")
    query.answer('No')







# if __name__ =='__main__':
#     app.run()
updater=Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Uzbek tili 🇺🇿'),uzbek_tili))
updater.dispatcher.add_handler(MessageHandler(Filters.text("Biz bilan bog'lanish"),aloqa))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Asosiy menu'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text("Ma'lumot olish"),malumot_uzbekcha))
updater.dispatcher.add_handler(MessageHandler(Filters.text('русский язык 🇷🇺'),ruscha))
updater.dispatcher.add_handler(MessageHandler(Filters.text('главное меню'), start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('связаться с нами'), aloqa_ruscha))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Получить информацию'), malumot_ruscha))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Rasmlari 📸'), photo_uzbekcha))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Ulchamlari va narxlari 💶'), money_uzbekcha))
updater.dispatcher.add_handler(MessageHandler(Filters.text('картинки 📸'), photo_ruscha))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Размеры и цены 💶'), money_ruscha))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Orqaga qaytish ◀️'),uzbek_tili))
updater.dispatcher.add_handler(MessageHandler(Filters.text('возвращаться ◀️'),ruscha))
updater.dispatcher.add_handler(CallbackQueryHandler(query))
updater.start_polling()
updater.idle()





