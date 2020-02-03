import speech_recognition as sr
import os
import time
import pyttsx3
import datetime
import webbrowser
import playsound
from random import choice

opts = {
    "alias": ("пит", "питон", "пайтон", "питоша", "питер",
              "питэр", "тварь", "пид"),
    "tbr": ("скажи", "расскажи", "покажи", "подскажи", 
            "сколько", "произнеси", "назови", "включи", "открой", "запусти"),
    "tbrphrases": {"включи": "Включаю...", "открой": "Открываю...", "запусти": "Запускаю..."},
    "cmds": {
        "hi": ('привет', 'здравствуйте', 'здравствуй'),
        "ctime": ('время', 'времени', 'час'),
        "music": ('музыку', 'музыка'),
        "stupid": ('анекдот', 'рассмеши'),
        "vk": ('в контакте', 'вконтакте', 'вк', 'vk'),
        "yt": ('youtube', 'ютуб'),
        "bye": ('пока', 'прощай', 'до свидания')
    }
}

JOKES = ["В борьбе с коррупцией главное - не победа, а участие...",
        "Хорошо, когда начальник замечает, как ты работаешь. Плохо только, что это бывает, когда ты не работаешь."]
comand = ""
TO_QUIT = False

def goodbye():
    speak("До новых встреч!")
    print("Выключение...")

#functions
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()
 
def callback(cmd):
    global comand
    for x in opts['alias']:
        cmd = cmd.replace(x, "").strip()

    for x in opts['tbr']:
        phrases = opts['tbrphrases'].keys()
        if x in cmd.lower() and x in phrases:
            cmd = cmd.replace(x, "").strip()
            phr = opts['tbrphrases'].get(x, 'Выполняю...')
            speak(phr)
    
    comand = cmd.lower()

    # распознаем и выполняем команду
    
    cmd = recognize_cmd(cmd)
    execute_cmd(cmd)
 
def recognize_cmd(cmd):
    cmd = cmd.lower().split()
    for word in cmd:
        for i in opts["cmds"]:
            if word in opts["cmds"][i]:
                return i
    
    return "search"
    
 
def execute_cmd(cmd):
    global TO_QUIT

    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        hour = str(now.hour)
        minute = str(now.minute)
        if len(minute) < 2:
            minute = "0" + minute
        speak("Сейчас " + hour + ":" + minute)
   
    elif cmd == 'hi':
        speak(choice(["И Вам здравствуйте", "И тебе привет", "Привет"]))

    elif cmd == 'bye':
        TO_QUIT = True


    elif cmd == 'music':
        try:
            with open('music.txt') as f:
                for line in f:
                    adress = line
            if "$$$" in adress:
                webbrowser.open_new(adress.split("$$$")[1])
            else:
                playsound.playsound(adress, True)

        except FileNotFoundError:
            speak('Указанного вами файла .mp3 не существует. Путь должен быть следующего вида: D:\music\Roses.mp3')
            #webbrowser.open_new("https://studio21.ru/radio/")
    
    
    elif cmd == 'vk':
        webbrowser.open_new("https://vk.com/feed")

    elif cmd == 'yt':
        webbrowser.open_new("https://www.youtube.com/")

    elif cmd == 'stupid':
        # рассказать анекдот
        speak(choice(JOKES))
   
    else:
        webbrowser.open_new("https://yandex.ru/search/?lr=12&clid=9403&oprnd=4358289752&text=" + comand)

def listen(index):
    r = sr.Recognizer()
    indexmicro = index
    micro = sr.Microphone(device_index = indexmicro)
    speak("Пит слушает. Скажите, что мне надо сделать:")
    with micro as source:
        audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio, language="ru-RU")
        print("Вы сказали: " + cmd)
        callback(cmd)
    except sr.UnknownValueError:
        speak("Извините, я Вас не расслышала")
        listen(index)
    if not TO_QUIT:
        print('Нажмите Enter, если хотите ещё что-то сказать. Напишите "стоп", если хотите выключить меня')
        a = input()
        if a.lower() != "стоп":
            listen(indexmicro)
        else:
            goodbye()
    else:
        goodbye()
    

 
speak_engine = pyttsx3.init()

speak("Добрый день, повелитель")

try:
    with open('index.txt', 'r') as f:
        index = f.read()

        try:
            if index in (str(i) for i in range(0, 11)):
                index = int(index)
            listen(index)

        except AssertionError:
            speak('Выберите микрофон в приложении micro.exe\nНе изменяйте файл index.txt вручную!')
            print('Выключение...')

        except OSError:
            speak('Неизвестная ошибка, связанная с выбранным микрофоном.\nВыберите микрофон в приложении micro.py и проверьте его работоспособность.')
            print('Выключение...')

except FileNotFoundError:
    speak('Выберите микрофон в приложении micro.exe')
    print('Выключение...')
