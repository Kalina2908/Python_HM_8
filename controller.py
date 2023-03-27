import view
import model

def run():
    view.hello()
    
    while True:
        view.menu()
        answer = input("Введите номер действия: ")
        if answer == "1":
            view.show_phonebook()

        elif answer == "2":
            model.add_contact()

        elif answer == "3":
            view.show_find_contact()

        elif answer == "4":
            model.change_contact()

        elif answer == "5":
            model.delete_contact()

        elif answer == "6":
            view.bye_phonebook()
            break
