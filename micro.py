import speech_recognition as sr


NOT_MICRO = ["переназначение", "первичный", "драйвер", "динамики", "nvidia"]
MICRO = True
indexes = []
names = []

def mindex():
    global MICRO
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if index > 10:
            break

        for word in NOT_MICRO:
            if word in name.lower():
                MICRO = False

        if MICRO:
            if name not in names:
                print("Микрофон \"{1}\" найден с индексом {0}".format(index, name))
                indexes.append(str(index))
                names.append(name)
        else:
            MICRO = True

    index = input("Введите индекс своего микрофона: ")

    if index in indexes:
        with open('index.txt', 'w') as f:
            f.write(index)
            print('ok')
    else:
        print('Вы ввели некорректный индекс!')
        mindex()

mindex()
