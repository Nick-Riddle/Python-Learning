import json
import os
import urllib.request

import telebot
from acrcloud.recognizer import ACRCloudRecognizer
from bs4 import BeautifulSoup as bs
from config import *
from selenium import webdriver
from telebot import types

acrcloud = ACRCloudRecognizer(config)

bot = telebot.TeleBot(TOKEN)

keyboard_yes_no = types.InlineKeyboardMarkup()
key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
keyboard_yes_no.add(key_yes)
key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
keyboard_yes_no.add(key_no)

keyboard_searching = types.InlineKeyboardMarkup()
key_search = types.InlineKeyboardButton(text='Искать', callback_data='search')
keyboard_searching.add(key_search)
key_not_search = types.InlineKeyboardButton(
    text='Не надо', callback_data='not_search')
keyboard_searching.add(key_not_search)


@bot.message_handler(commands=['start'])
def welcome_start(message):
    bot.send_message(
        message.from_user.id,
        f'Приветствую тебя @{message.from_user.username}')


@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(
        message.from_user.id,
        'Привет, ты готов к работе со мной?',
        reply_markup=keyboard_yes_no)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Я тебя не понимаю, напиши /help.')


@bot.message_handler(content_types=['audio'])
def get_audio_messages(message):
    audio_id = message.audio.file_id
    file_info = bot.get_file(audio_id)
    urllib.request.urlretrieve(
        f'http://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}',
        file_info.file_path)
    file_path = r'C:\Users\kolya\Python-Learning\Python_learning\Projects\telegram_bot\\' + \
                file_info.file_path
    get_audio_info(message, acrcloud.recognize_by_file(file_path, 0))
    os.remove(file_path)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id,
                         'Ну, тогда начнем!\nОтправь мне файл с музыкой.')
    elif call.data == 'no':
        bot.send_message(
            call.message.chat.id,
            'Привет, ты готов к работе со мной?',
            reply_markup=keyboard_yes_no)
    elif call.data == 'search':
        search_link = "http://www.youtube.com/results?search_query=" + \
                      '+'.join([title, artist])
        driver = webdriver.Chrome()
        driver.get(search_link)
        html = driver.page_source
        driver.close()
        soup = bs(html, "html.parser")
        videos = soup.find_all("ytd-thumbnail",
                               {"class": "style-scope ytd-video-renderer"})
        link = 'youtube.com/' + \
               videos[0].find('a', {'id': 'thumbnail'}).get('href')
        bot.send_message(
            call.message.chat.id,
            f'Вот, что я нашел.\nYouTube: {link}')
    elif call.data == 'not_search':
        bot.send_message(call.message.chat.id, 'Хорошо.')
    bot.edit_message_reply_markup(
        call.message.chat.id,
        call.message.message_id)


def get_audio_info(message, data):
    global title, artist
    spotify = None
    data = json.loads(data)
    if data['status']['msg'] == 'Success':
        data = data['metadata']['music']
        for d in data:
            if 'spotify' in d['external_metadata']:
                data = d
                break
            else:
                data = d
        title = data['title']
        artist = data['artists'][0]['name']
        try:
            spotify = 'open.spotify.com/track/' + \
                      data["external_metadata"]["spotify"]["track"]["id"]
        except KeyError:
            bot.send_message(
                message.from_user.id,
                'Я не смог найти эту песню на Spotify, но я могу постараться поискать на YouTube, но это может быть безуспешно...',
                reply_markup=keyboard_searching)
        if spotify is not None:
            bot.send_message(
                message.from_user.id,
                f'Я нашел.\nИмя песни: {title}.\nИсполнитель: {artist}.\n\nSpotify: {spotify}')


bot.polling(none_stop=True, interval=0)
