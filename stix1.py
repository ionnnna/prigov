import telebot
from telebot import types
import random

bot = telebot.TeleBot('1323327743:AAHlm0QsWNAyPkJcmNJmxXk9Tr4gGxctp7w')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Дмитрий Алексаныч!')
city_list = ['Веник сломан, не фурычит \n Нечем пол мне подметать \n А уж как, едрена мать \n Как бывало подметал я \n Там, бывало, подмету - \n Все светло кругом, я ныне \n Сломано все, не фурычит \n Жить не хочется',
			 'Прости меня, я умираю \n Врачи мне вырезали печень \n И съели \n И следом мозг - чтоб мыслить нечем \n Было \n Тоже съели \nМне это показалось раем \n Поначалу \n Все перестало вдруг вертеться \n Повисло тихое! Но сердце \n Сердце! сердце! сердце! \n Бедное! \n Все страдает ',
			 'Только вымоешь посуду \n Глядь - уж новая лежит \n Уж какая тут свобода \n Тут до старости б дожить \n Правда, можно и не мыть \n Да вот тут приходят разные \n Говорят: посуда грязная - \n Где уж тут свободе быть',
			 'Вот в очереди тихонько стою  \n И думаю себе отчасти: \n Вот Пушкина бы в очередь сию \n И Лермонтова в очередь сию \n И Блока \n О чем писали бы? - о счастье',
			 'Закон ученый открывает \n Другой приходит – отменяет \n А тот хватает пистолет \n И гада в сердце убивает \n Поскольку вот – закона нет \n Кроме страсти человечьей \n И милосердия ',
			 'Мама временно ко мне \nВъехала на пару дней \n Вот я представляю ей: \n Это кухня, туалет \n Это мыло, это ванна \n А вот это тараканы \n Тоже временно живут \n Мама молвит неуверенно: \n Правда временно живут? - \n Господи, да все мы временны!'



			 ]

@bot.message_handler(commands=['start', 'stixi'])
def send_welcome(message):
	bot.reply_to(message, "Товарищи!", reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == "Дмитрий Алексаныч!":
        bot.send_message(message.chat.id, random.choice(city_list))

bot.polling()