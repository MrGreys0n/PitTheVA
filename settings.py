import os


def menu():
    print("1. Адрес сайта с музыкой или расположение музыки на компьютере.\n" +
          "2. Голос помощника.\n" +
          "3. Выйти.")

musicAdress = ""
site = False
while True:
    menu()
    a = input("Введите номер: ")
    if a == '1':
        while True:
            print("1. Сайт.\n2. Музыка на компьютере.")
            b = input("Введите номер: ")
            if b == "1":
                musicAdress = input("Введите адрес сайта: ")
                print("OK")
                site = True
                break
            elif b == "2":
                musicAdress = input("Введите расположение музыки (только латиница, путь до файла .mp3, включая само имя файла): ")
                print("OK")
                break
            else:
                print("Вы ввели некорректный номер!")
    elif a == '2':
        print('В данной версии приложения изменение голоса помощника невозможно.')
        break
    elif a == '3':
        print('ok')
        break
    else:
        print("Вы ввели некорректный номер!")

if len(musicAdress) > 0:
    '''fileadr = os.path.abspath(__file__)
    fileadr = fileadr.replace(':', '')
    print(fileadr)
    mustxt = fileadr + '\\' + 'music.txt'
    mustxt = mustxt.replace('\\', '//')'''

    with open('music.txt', 'w') as f:
        if site:
            f.write("site$$$")
        f.write(musicAdress)

print('Сохранение настроек...')