import speech_recognition as sr

def mindex():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if index > 5:
            break
        print("Микрофон с именем \"{1}\" найден с (device_index={0})".format(index, name))
    index = input("Введите device_index своего микрофона одной цифрой: ")
    if index in ('0', '1', '2', '3', '4', '5'):
        with open('index.txt', 'w') as f:
            f.write(index)
            print('ok')
    else:
        print('Вы ввели некорректный device_index!')
        mindex()

mindex()
