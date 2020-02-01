import speech_recognition as sr
import os
import time
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser
from random import choice

opts = {
    "alias": ("пит", "питон", "пайтон", "питоша", "питер",
              "питэр", "тварь", "пид"),
    "tbr": ("скажи", "расскажи", "покажи", "подскажи", 
            "сколько", "произнеси", "назови", "включи", "открой", "запусти"),
    "tbrphrases": {"включи": "Включаю...", "открой": "Открываю...", "запусти": "Запускаю..."},
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'который час'),
        "music": ('музыку', 'музыка'),
        "stupid": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдот'),
        "vk": ('в контакте', 'вконтакте', 'вк', 'vk'),
        "yt": ('youtube', 'ютуб')
    }
}

#functions
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()
 
def callback(cmd):
    for x in opts['alias']:
        cmd = cmd.replace(x, "").strip()

    for x in opts['tbr']:
        if x in cmd:
            cmd = cmd.replace(x, "").strip()
            if x in opts['tbrphrases']:
                speak(opts['tbphrases'][x])

    # распознаем и выполняем команду
    cmd = recognize_cmd(cmd)
    execute_cmd(cmd['cmd'])
 
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
   
    return RC
 
def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        hour = str(now.hour)
        minute = str(now.minute)
        if len(minute) < 2:
            minute = "0" + minute
        speak("Сейчас " + hour + ":" + minute)
   
    elif cmd == 'music':
        # воспроизвести радио
        speak(choice(['Открываю...', 'Включаю...', 'Запускаю...']))
        webbrowser.open_new("https://studio21.ru/radio/")
    
    elif cmd == 'vk':
        speak('Открываю...')
        webbrowser.open_new("https://vk.com/feed")

    elif cmd == 'yt':
            speak('Открываю...')
            webbrowser.open_new("https://www.youtube.com/")

    elif cmd == 'stupid':
        # рассказать анекдот
        speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
   
    else:
        print('Команда не распознана, повторите!')

def listen(index):
    r = sr.Recognizer()
    indexmicro = index
    micro = sr.Microphone(device_index = indexmicro)
    speak("Пит слушает. Скажите, что мне надо сделать:")
    with micro as source:
        audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio, language="ru-RU")
        print("Вы сказали: " + cmd.lower())
        callback(cmd)
    except sr.UnknownValueError:
        speak("Извините, я Вас не расслышала")
        listen(index)
    print('Нажмите Enter, если хотите ещё что-то сказать. Напишите "стоп", если хотите выключить меня')
    a = input()
    if a.lower() != "стоп":
        listen(indexmicro)
    else:
        speak("До новых встреч!")
        print("Выключение...")
    
 
# запуск
#r = sr.Recognizer()
 
speak_engine = pyttsx3.init()

speak("Добрый день, повелитель")

try:
    with open('index.txt', 'r') as f:
        index = f.read()
        if len(index) == 1:
            index = int(index)
        listen(index)
except FileNotFoundError:
    speak('Выберите микрофон в приложении micro.exe')
