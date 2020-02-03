import os
# После запуска программы пользователь видит меню, состоящее из следующих пунктов:
#
#  1- создать папку;
#  2- удалить (файл/папку);
#  3- копировать (файл/папку);
#  4- просмотр содержимого рабочей директории;
#  5- посмотреть только папки;
#  6- посмотреть только файлы;
#  7- просмотр информации об операционной системе;
#  8- создатель программы;
#  9- играть в викторину;
# 10- мой банковский счет;
# 11- смена рабочей директории (*необязательный пункт);
# 12- выход.
#
# После выполнения какого либо из пунктов снова возвращаемся в меню, пока пользователь не выберет выход
#

# 1
def my_create(folder_name):
    os.mkdir(folder_name)


# 2
def my_delete():
    pass


# 3
def my_copy():
    pass


#f 4
def my_print_list():
    pass


# 5
def my_print_folders():
    pass


# 6
def my_print_files():
    pass


# 7
def my_os_info():
    pass


# 8
def my_print_author():
    pass


# 9
def my_victory_game():
    pass


# 10
def my_bill():
    pass


# 11
def my_change_dir():
    pass

# 12  Exit !


def show_menu():
    path = os.getcwd()
    print(path)

    print(' 1- Создать папку')
    print(' 2- Удалить (файл/папку)')
    print(' 3- Копировать (файл/папку)')
    print(' 4- Просмотр содержимого рабочей директории')
    print(' 5- Посмотреть только папки')
    print(' 6- Посмотреть только файлы')
    print(' 7- Просмотр информации об операционной системе')
    print(' 8- Создатель программы')
    print(' 9- Играть в викторину')
    print('10- Мой банковский счет')
    print('11- Смена рабочей директории')
    print('12- Выход')
    item = input('Выберите пункт меню: ')
    return item


def main_menu():
    while True:
        choice = int(show_menu())
        if choice == 1:
            my_create()
        elif choice == 2:
            my_delete()
        elif choice == 3:
            my_copy()
        elif choice == 4:
            my_print_list()
        elif choice == 5:
            my_print_folders()
        elif choice == 6:
            my_print_files()
        elif choice == 7:
            my_os_info()
        elif choice == 8:
            my_print_author()
        elif choice == 9:
            my_victory_game()
        elif choice == 10:
            my_bill()
        elif choice == 11:
            my_change_dir()
        elif choice == 12:
            break


if __name__ == '__main__':
    main_menu()