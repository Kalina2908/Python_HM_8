import model 

def hello():
    print("Приветствуем Вас в телефонном справочнике.")
    


def menu():
    print("Действия, которые Вы можете выполнить:")
    print("1. Просмотр телефонного справочника")
    print("2. Добавление контакта")
    print("3. Поиск контакта")
    print("4. Изменить данные")
    print("5. Удалить данные")
    print("6. Выйти")


def show_phonebook():
    f = open('file_name.txt','r')
    print (*f)
    f.close()

def bye_phonebook():
    print ('До свидания!')

def show_find_contact():
    find_data = input('Введите данные, которые Вы ищите:')
    data = model.find_contact(find_data)
    if data != None:
        print(data)
        print('')
    else:
        print("Контакт не найден")
        print('')