# pip install pyTelegramBotAPI
import random
import telebot 
from telebot import types
import os
import schedule
from threading import Thread
from time import sleep

file = open('support.txt', 'r', encoding='utf-8')
support = file.read().split('\n')
file.close()

bot = telebot.TeleBot('6640190707:AAFdcztStYE0YzgFqFdRpwWTgsJIMdSKhG0')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('распустил нюни')
    item2 = types.KeyboardButton('опустил крылья')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Как себя чувствуешь?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_handle_text(message):

    if message.text.strip() == 'распустил нюни' or message.text.strip() == 'Еще!!!':
        answer = random.choice(support)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Еще!!!')
        item2 = types.KeyboardButton('Супер!')
        item3 = types.KeyboardButton('опустил крылья')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, answer, reply_markup=markup)
    elif message.text.strip() == 'опустил крылья':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Супер!')
        markup.add(item1,)
        bot.send_message(message.chat.id, 'я напишу тебе еще', reply_markup=markup)
        user_id = message.from_user.id
        def function_to_run():
            bot.send_message(user_id, random.choice(support))
        schedule.every(60).minutes.do(function_to_run)
    elif message.text.strip() == 'Супер!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('распустил нюни')
        item2 = types.KeyboardButton('опустил крылья')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Так держать👍🏽', reply_markup=markup)
        schedule.clear()
    else:
        bot.send_message(message.chat.id, 'Ой... что-то тут лишнее. Советую пользоваться кнопками из меню')


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


Thread(target=schedule_checker).start()


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()