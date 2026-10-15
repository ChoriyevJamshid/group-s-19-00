import telebot


API_TOKEN = "8689121919:AAHQ-Z2FczKIJ2EP88yZxm_2z51h3_pcDQA"

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler( commands=["start"] )
def start_handler(message):
    
    answer_message = (
        "Assalomu alaykum, Salom Dunyo botiga xush kelibsiz!"
    )
    bot.reply_to(message, answer_message)


@bot.message_handler( commands=["id"] )
def id_handler(message):
    
    chat_id = message.chat.id
    answer_message = f"Sizning chat id raqamingiz: {chat_id}"
    bot.reply_to(message, answer_message)


@bot.message_handler( commands=["vazifa"] )
def vazifa_handler(message):
    
    if message.chat.id != 2124744962:
        answer_message = "Siz admin emassiz, vazifani faqat admin olishi mumkin!"
        bot.reply_to(message, answer_message)
        return 
    
    answer_message = (
        "Sizga vazifa berildi!\n"
        "Vazifa: 1 dan 10 gacha bo'lgan sonlarni ekranga chiqarish dasturini yozing."
    )
    bot.reply_to(message, answer_message)




@bot.message_handler()
def echo_handler(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()



