def add_contact():
    f = open('file_name.txt','a')
    name_first = input('Напишите имя: ')
    name_last = input('Напишите фамилию: ')
    phone_number = input('Напишите номер:')
    f.write(name_first + ' ')
    f.write(name_last + ' ')
    f.write(phone_number + '\n')
    f.close()
    print(f"Новый контакт {name_first} {name_last} записан")
    print('')

def add_new_contact():
    f = open('file_name.txt','r+')
    name_first = input('Напишите имя: ')
    name_last = input('Напишите фамилию: ')
    phone_number = input('Напишите номер:')
    added_contact = name_first + ' ' + name_last + ' ' + phone_number + '\n'
    f.close()
    return added_contact
    

def find_contact(data):
    f = open ('file_name.txt', 'r')
    count = None
    for line in f:
        if data in line:
            count = line
    f.close()
    return count


def change_contact():
    change_data = input('Введите контакт, который Вы хотите изменить:')
    data = find_contact(change_data)
    if data == None:
        print("Контакт не найден")
        print('')
    else:
        new_information = add_new_contact()
        with open ('file_name.txt', 'r+') as f:
            old_data = f.read()
            new_data = old_data.replace(data, new_information)

        with open ('file_name.txt', 'w') as f:
            f.write(new_data)
            print(("Новые данные контакта внесены"))
            print('')


def delete_contact():
    delete_data = input('Введите данные, которые Вы хотите удалить:')
    data = find_contact(delete_data)
    if data == None:
        print("Контакт не найден")
        print('')
    else:
        information_data = ""
        with open ('file_name.txt', 'r+') as f:
            old_data = f.read()
            new_data = old_data.replace(data, information_data)

        with open ('file_name.txt', 'w') as f:
            f.write(new_data)
            print(("Контакт удален"))
            print('')