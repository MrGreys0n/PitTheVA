import speech_recognition as sr

def mindex():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if index > 5:
            break
        if index % 2 == 1:
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    index = input("Введите device_index своего микрофона одной цифрой: ")
    if index in ('1', '3', '5'):
        return(int(index))
    else:
        print('Вы ввели некорректный device_index!')
        mindex()