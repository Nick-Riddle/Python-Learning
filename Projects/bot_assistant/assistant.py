from pyowm.utils.config import get_default_config
from translate import Translator
from datetime import datetime
import speech_recognition as speech_recog
import requests as req
import webbrowser
import wikipedia
import pyttsx3
import ctypes
import random
import pyowm
import os


class Assistant:
    name = ''
    sex = ''
    speech_lang = ''
    recog_lang = ''


def get_location_json():
    geo_req = req.get(
        'http://api.ipstack.com/178.159.209.2?access_key=9c8077d3aa04f28220c07c4998515d3b')
    return geo_req.json()


def assistant_installation():

    voices = engine.getProperty('voices')

    if assistant.speech_lang == 'en' and assistant.name == 'Zira':
        assistant.recog_lang = 'en-US'
        engine.setProperty('voice', voices[1].id)
    else:
        assistant.recog_lang = 'ru-RU'
        engine.setProperty('voice', voices[0].id)


def assistant_voice(text):

    engine.say(text)
    engine.runAndWait()


def recording_and_recognizing_audio():

    with microphone as audio_file:
        data_input = ''

        recognizer.adjust_for_ambient_noise(audio_file, duration=2)

        try:
            assistant_voice('Говорите...')
            audio = recognizer.listen(audio_file)
        except speech_recog.WaitTimeoutError:
            return recording_and_recognizing_audio()

        try:
            print('Распознаю речь...')
            data_input = recognizer.recognize_google(
                audio, language='ru').lower()
        except speech_recog.UnknownValueError:
            pass
        except speech_recog.RequestError:
            assistant_voice('Проверьте подключение к интернету.')
            return recording_and_recognizing_audio()

        return data_input


if __name__ == '__main__':

    recognizer = speech_recog.Recognizer()
    microphone = speech_recog.Microphone()

    engine = pyttsx3.init()

    assistant = Assistant()
    assistant.name = 'Irina'
    assistant.sex = 'female'
    assistant.speech_lang = 'ru'

    assistant_installation()

    assistant_voice('Пожалуйста, скажите мне свое имя.')
    name = recording_and_recognizing_audio()
    assistant_voice('Я его запомню.')

    while True:

        voice_input = recording_and_recognizing_audio()
        if not voice_input:
            continue

        first_words = voice_input.split()[:2]

        if 'привет' in voice_input or 'здравствуй' in voice_input or 'здравствуйте' in voice_input or 'хай' in voice_input:
            if datetime.now().hour < 12:
                assistant_voice(f'Доброе утро, {name}')
            elif datetime.now().hour < 18:
                assistant_voice(f'Добрый день, {name}')
            else:
                assistant_voice(f'Добрый вечер, {name}')

        elif 'открой' in voice_input:
            translator = Translator(from_lang="russian", to_lang="english")
            domain = translator.translate(''.join(voice_input.split()[1:]))
            print(domain)
            url = webbrowser.open('https://www.' + domain + '.com')

        elif 'расскажи про' in voice_input:
            wikipedia.set_lang('ru')
            try:
                assistant_voice(wikipedia.page(
                    ' '.join(voice_input.split()[2:])).content[:100])
            except wikipedia.exceptions.WikipediaException:
                assistant_voice(
                    'К сожалению я не могу вам рассказать об этом.')

        elif 'поменять обои' in voice_input or 'поменяй обои' in voice_input:
            assistant_voice('Меняю обои, одну секунду...')
            SPI_SETDESKWALLPAPER = 20
            images = os.listdir(r'C:\Users\kolya\Python-Learning\images')

            temp = -1
            random_img = random.randrange(len(images))
            while temp == random_img:
                random_img = random.randrange(len(images))
            temp = random_img

            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER,
                0,
                r'C:\Users\kolya\Python-Learning\images\\' +
                images[random_img],
                3)
            assistant_voice('Обои успешно заменены.')

        elif 'текущая погода' in voice_input or 'скажи погоду' in voice_input:
            config_dict = get_default_config()
            config_dict['language'] = 'ru'
            owm = pyowm.OWM('ab0d5e80e8dafb2cb81fa9e82431c1fa', config_dict)
            manager = owm.weather_manager().weather_at_place(
                get_location_json()['region_name'])
            weather = manager.weather
            temperature = weather.temperature(unit='celsius')
            status = weather.detailed_status
            assistant_voice(
                f'Сейчас в {get_location_json()["region_name"]} {status}, температура на улице {round(temperature["feels_like"])} градусов по Цельсию.')

        elif 'скажи время' in voice_input:
            assistant_voice(
                f'В {get_location_json()["country_name"]} сейчас {datetime.now().hour} часов {datetime.now().minute} минут.')

        elif 'заверши' in voice_input or 'завершить' in voice_input or 'выход' in voice_input or 'выйти' in voice_input:
            assistant_voice(f'До следующей встречи, {name}')
            break
