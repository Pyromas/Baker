import telebot
from telebot import types 

bot = telebot.TeleBot('7297462324:AAGNG73dosVDWqA7n04oNY_xYzADhmyguhU')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("Страна")
    markup.add(btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я - Бот для помощи в кулинарии. Пожалуйста, выберите команду (страна) что бы продолжить.".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Страна"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🍙Китай")
        btn2 = types.KeyboardButton("🥖Франция")
        btn3 = types.KeyboardButton("🍲Украина")
        btn4 = types.KeyboardButton("🍕Италия")
        btn5 = types.KeyboardButton("🐟Норвегия")
        btn6 = types.KeyboardButton("🥨Германия")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6,  back)
        bot.send_message(message.chat.id, text="Пожалуйста выберите страну", reply_markup=markup)
    
    elif(message.text == "🍙Китай"):
        bot.send_message(message.chat.id, "Here go to this site and cook you breakfeast https://svet-vostoka.ru/blog/kak-zavtrakajut-v-kitae/.Here is a lunch https://www.russianfood.com/recipes/bytype/?fid=132,927.")
    
    elif message.text == "🥖Франция":
        bot.send_message(message.chat.id, text="Here go to this site and cook you breakfeast https://paris10.travel/chto-sest-na-zavtrak-v-parizhe/.Here is a lunch https://www.irk.ru/obed/articles/20121029/france/")

    elif message.text == "🍲Украина":
        bot.send_message(message.chat.id, text="Here go to this site and cook you breakfeast https://elle.ua/ru/stil-zhizni/food/kulinarnoe-nasledie-tradicionnie-ukrainskie-zavtraki/.Here is a lunch https://milkalliance.com.ua/blog/ru/statya/chto-prigotovit-na-obed-luchshie-blyuda-ukrainskoj-kukhni")

    elif message.text == "🍕Италия":
        bot.send_message(message.chat.id, text="Here go to this site and cook you breakfeast https://eda.ru/recepty/zavtraki/italyanskaya-kuhnya.Here is a lunch https://www.russianfood.com/recipes/bytype/?fid=110,927")

    elif message.text == "🐟Норвегия":
        bot.send_message(message.chat.id, text="Here go to this site and cook you breakfeast https://www.gastronom.ru/recipe/40483/norvezhskij-zavtrak.Here is a lunch https://lidaleko.livejournal.com/22450.html")

    elif message.text == "🥨Германия":
        bot.send_message(message.chat.id, text="Here go to this site and cook you breakfeast https://www.iamcook.ru/section/13720.Here is a lunch https://www.iamcook.ru/section/13719") 

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Страна")
        markup.add(btn2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)
