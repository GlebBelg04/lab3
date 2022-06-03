# Телеграм-бот v.003 - бот подбирает картинки и тексты с поздравлениями
import telebot  # pyTelegramBotAPI 4.3.1
import telebot  # pyTelegramBotAPI 4.3.1
from telebot import types
import requests
import bs4   #beautifulsoup4

bot = telebot.TeleBot('5151755926:AAG44-dQV2qGf0kUfJfbvjIfMFP_SJFY1Ig')

# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я бот, который подбирает картинки и тесты с поздравлениями на любой праздник!".format(
                         message.from_user), reply_markup=markup)


# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "👋 Главное меню" or ms_text == "Вернуться в главное меню":  # ..........
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Картинки")
        btn2 = types.KeyboardButton("Позравления")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Картинки":  # ..................................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("День рождения")
        btn2 = types.KeyboardButton("8 марта")
        back = types.KeyboardButton("23 февраля")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Картинки", reply_markup=markup)

    elif ms_text == "День рождения":  # .........................................................
        bot.send_photo(chat_id, photo=get_dogURL(), caption="Вот тебе позравление с Днем Рождения!")

    elif ms_text == "8 марта":  # .............................................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "23 февраля":  # .............................................................................
        bot.send_message(chat_id, text="еще не готово...")



    elif ms_text == "Позравления":  # ..................................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("День рождения")
        btn2 = types.KeyboardButton("8 марта")
        back = types.KeyboardButton("23 февраля")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Поздравления", reply_markup=markup)

    elif ms_text == "День рождения":  # .........................................................
        bot.send_photo(chat_id,

    elif ms_text == "8 марта":  # .............................................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "23 февраля":  # .............................................................................
        bot.send_message(chat_id, text="еще не готово...")



    elif ms_text == "Помощь" or ms_text == "/help":  # .................................................................
        bot.send_message(chat_id, "Автор: Я")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/dmlarionova")
        key1.add(btn1)
        img = open('AVA.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)


    else:  # ...........................................................................................................

        bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)

    # -----------------------------------------------------------------------

    bot.polling(none_stop=True, interval=0)  # Запускаем бота

    print()