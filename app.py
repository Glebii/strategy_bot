#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from config import TOKEN
from config import first, second, third, fourth, fifth, fk_free_text, fk_pay_text, sk_free_text, sk_pay_text, fifthk_free_text, fifthk_pay_text,start_text1, start_text2, third_text, fourth_text
from telebot import types

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row(first)
keyboard.row(second)
keyboard.row(third)
keyboard.row(fourth)
keyboard.row(fifth)

@bot.message_handler(commands=['start'])
def start_message(message):
    
    bot.send_message(message.chat.id, start_text1, reply_markup=keyboard)
    bot.send_message(message.chat.id, start_text2, reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_message(message): 

    firstkeyboard = types.InlineKeyboardMarkup(row_width=2)
    fk_first_button = types.InlineKeyboardButton(text='Дама любой масти', callback_data='fk_free')
    fk_second_button = types.InlineKeyboardButton(text='Любая точная карта', callback_data='fk_pay')
    firstkeyboard.add(fk_first_button, fk_second_button)
    
    secondkeyboard = types.InlineKeyboardMarkup(row_width=2)
    sk_first_button = types.InlineKeyboardButton(text='Определение по предыдущим мастям', callback_data='sk_free')
    sk_second_button = types.InlineKeyboardButton(text='Масть с проходом 99%', callback_data='sk_pay')
    secondkeyboard.row(sk_first_button)
    secondkeyboard.row(sk_second_button)
    

    fifthkeyboard = types.InlineKeyboardMarkup(row_width=2)
    fifthk_first_button = types.InlineKeyboardButton(text='Ориентировка на тотал по коэффиценту дилера', callback_data='fifthk_free')
    fifthk_second_button = types.InlineKeyboardButton(text='Точный тотал на игрока, дилера и общий тотал', callback_data='fifthk_pay')
    fifthkeyboard.row(fifthk_first_button)
    fifthkeyboard.row(fifthk_second_button)
 

    if message.text == first:
        bot.send_message(message.chat.id, 'Выбирай⤵️', reply_markup=firstkeyboard)  
    
    elif message.text == second:
        bot.send_message(message.chat.id, 'Выбирай⤵️', reply_markup=secondkeyboard)

    elif message.text == fifth:
        bot.send_message(message.chat.id, 'Выбирай⤵️', reply_markup=fifthkeyboard)  
    
    elif message.text == fourth:
        bot.send_message(message.chat.id, fourth_text, reply_markup=keyboard)

    elif message.text == third:
        bot.send_message(message.chat.id, third_text, reply_markup=keyboard)  

    else:
        bot.send_message(message.chat.id, 'Хей! Видимо ты ввел что-то не то...', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    
#-----FIRTSKEYBOARD--------------------------------------------------------------------------

    if call.data == 'fk_mainmenu':
        firstkeyboard = types.InlineKeyboardMarkup(row_width=2)
        fk_first_button = types.InlineKeyboardButton(text='Дама любой масти', callback_data='fk_free')
        fk_second_button = types.InlineKeyboardButton(text='Любая точная карта', callback_data='fk_pay')
        firstkeyboard.add(fk_first_button, fk_second_button)
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбирай⤵️', reply_markup=firstkeyboard)        
    
    if call.data == 'fk_free':
        call_back_firstkeyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text='Назад', callback_data='fk_mainmenu')
        call_back_firstkeyboard.add(backbutton)
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=fk_free_text, reply_markup=call_back_firstkeyboard)        

    if call.data == 'fk_pay':
        call_back_firstkeyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text='Назад', callback_data='fk_mainmenu')
        call_back_firstkeyboard.add(backbutton)
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=fk_pay_text, reply_markup=call_back_firstkeyboard) 

#-----SECONDKEYBOARD--------------------------------------------------------------------------

    if call.data == 'sk_mainmenu':
        secondkeyboard = types.InlineKeyboardMarkup(row_width=2)
        sk_first_button = types.InlineKeyboardButton(text='Определение по предыдущим мастям', callback_data='sk_free')
        sk_second_button = types.InlineKeyboardButton(text='Масть с проходом 99%', callback_data='sk_pay')
        secondkeyboard.row(sk_first_button)
        secondkeyboard.row(sk_second_button)
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбирай⤵️', reply_markup=secondkeyboard)

    if call.data == 'sk_free':
        call_back_secondkeyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text='Назад', callback_data='sk_mainmenu')
        call_back_secondkeyboard.add(backbutton)
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=sk_free_text, reply_markup=call_back_secondkeyboard)           

    if call.data == 'sk_pay':
        call_back_secondkeyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text='Назад', callback_data='sk_mainmenu')
        call_back_secondkeyboard.add(backbutton)
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=sk_pay_text, reply_markup=call_back_secondkeyboard)

#-----FIFTHKEYBOARD--------------------------------------------------------------------------

    if call.data == 'fifthk_mainmenu':
        fifthkeyboard = types.InlineKeyboardMarkup(row_width=2)
        fifthk_first_button = types.InlineKeyboardButton(text='Ориентировка на тотал по коэффиценту дилера', callback_data='fifthk_free')
        fifthk_second_button = types.InlineKeyboardButton(text='Точный тотал на игрока, дилера и общий тотал', callback_data='fifthk_pay')
        fifthkeyboard.row(fifthk_first_button)
        fifthkeyboard.row(fifthk_second_button)
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбирай⤵️', reply_markup=fifthkeyboard)
    
    if call.data == 'fifthk_free':
        call_back_fifthkeyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text='Назад', callback_data='fifthk_mainmenu')
        call_back_fifthkeyboard.add(backbutton)
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=fifthk_free_text, reply_markup=call_back_fifthkeyboard)           

    if call.data == 'fifthk_pay':
        call_back_fifthkeyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text='Назад', callback_data='fifthk_mainmenu')
        call_back_fifthkeyboard.add(backbutton)
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=fifthk_pay_text, reply_markup=call_back_fifthkeyboard)

bot.polling() 
