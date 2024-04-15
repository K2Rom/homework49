# Создать телефонный справочник с # возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер # телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной 


'''
проверяется наличие файла, его первая строка - заголовок, при отсутствии или несоответствии файл создается заново
'''
def test_file_dictionary(name_field,file_name):
    if (path.exists(file_name)):
        data = open(file_name,"r",encoding='utf-8')
        title = data.readline()
        data.close()
        if (title == name_field ):
            print("Файл справочника существует- Dictionary.txt")
        else:
            data = open(file_name,'w', encoding='utf-8')
            data.writelines(name_field)
            data.close()
            print("Файл справочника неверного формата\nCоздан пустой справочник - Dictionary.txt ")
            return
    else:
        print("Cправочник отсутствует, создан пустой справочник - Dictionary.txt")
        data = open(file_name,'w', encoding='utf-8')
        data.writelines(name_field)
        data.close()
        return

'''
ввод нового контакта
'''
def input_contact(name_fild):
    list_contact = list()
    print(name_field)
    print("Введите данные контакта", len(name_fild))
    for i in range(len(name_fild)):
        fild_i = str(input((name_fild[i])+": "))
        list_contact.append(fild_i)
    return(list_contact)

'''
печать справочника
'''
def print_dictionary(file_name):
    data = open(file_name,"r",encoding='utf-8')
    title = data.readline()
    count = 0
    print("------------------------------------")
    print("№№", title[:-1])
    print("------------------------------------")
    title = data.readline()
    while len(title) > 1:
        count += 1
        print(count, title[:-1])
        title = data.readline()
        if count % 10 == 0:
            print("       ....для продолжения печати нажмите клавишу")
            msvcrt.getch()        
    data.close()
    print("------------------------------------")
    print("Справочник распечатан\nНажмите клавишу, чтобы продолжить")
    msvcrt.getch()
    return    

'''
Добавление контакта без проверки наличия 
'''
def add_contact(file_name):
    data = open(file_name,"r",encoding='utf-8')
    line1 = data.readline()
    data.close()
    title = line1.split()
    line = str()
    print("Введите значения параметров для справочника")
    for i in range(len(title)):
        param = input(title[i]+": ")
        line = line + str(param) + " "
    line = line + "\n"
    data = open(file_name,"a",encoding='utf-8')
    data.writelines(line)
    data.close()
    print(f"Контакт {line} добавлен\nНажмите клавишу, чтобы продолжить")
    msvcrt.getch()
    return

'''
поиск пользователя по одному из параметров:фамилия, имя и номер телефона
'''
def  find_user(file_name,pozition):
    find_word = input()
    data = open(file_name,"r",encoding='utf-8')
    line1 = data.readline()
    line1 = data.readline()
    count = 0
    find_true = False
    while len(line1) > 1:
        count += 1
        line = line1.split()
        if line[pozition] == find_word:
            print(count, line1[:-1])
            find_true = True
        line1 = data.readline()
    if find_true == False:
        print("Контакт не найден")
    data.close()
    print("\n")
    print("Нажмите клавишу, чтобы продолжить")
    msvcrt.getch()
    return

'''
перезапись контакта в новый файл. имея файла - номер записи
'''
def rewrite_contact(file_name):
    number_str = int(input("Введите номер записи c 1: "))    
    if number_str < 1:
        print("Недопустимый номер записи")
        return
    data = open(file_name,"r",encoding='utf-8')
    title = data.readline()
    line1 = data.readline()
    count = 0
    find_true = False
    while len(line1) > 0:
        count += 1
        if count == number_str:
            data.close()
            new_filename = str(number_str)+".txt"
            data = open(new_filename,"w",encoding='utf-8')
            data.writelines(title)
            data.writelines(line1)
            data.close()
            print("Контакт скопирован в файл ",new_filename)
            print("Нажмите клавишу, чтобы продолжить")
            msvcrt.getch()
            return
        line1 = data.readline()
    data.close()
    print(f"\nЗапись с номером {number_str} не найдена")
    print("Нажмите клавишу, чтобы продолжить")
    msvcrt.getch()
    return

'''
Перезапись контакта в имеющийся файл
'''
def rewrite_in_oldfile(file_name):
    number_str = int(input("Введите номер записи в справочнике c 1: "))    
    if number_str < 1:
        print("Недопустимый номер записи")
        return
    data1 = open(file_name,"r",encoding='utf-8')
    title = data1.readline()
    line1 = data1.readline()
    count = 0
    find_true = False
    while len(line1) > 0:
        count += 1
        if count == number_str:
            data1.close()
            old_filename = input("Введите имя файла, в который записать контакт:")
            if (path.exists(old_filename)):
                data2 = open(old_filename,"a",encoding='utf-8')
                data2.writelines(line1)
                print("Файл дописан")
            else:
                data2 = open(old_filename,"w",encoding='utf-8')
                data2.writelines(title)
                data2.writelines(line1)
                print("Файл отсутствовал и был создан")
            data2.close()
            print("Нажмите клавишу, чтобы продолжить")
            msvcrt.getch()
            return
        line1 = data1.readline()
    data1.close()
    print(f"\nЗапись с номером {number_str} не найдена")
    print("Нажмите клавишу, чтобы продолжить")
    msvcrt.getch()
    return    

    
    old_filename = input("Введите имя файла, в который записать контакт:")
    if (path.exists(old_filename)):
        data = open(file_name,"r",encoding='utf-8')
        title = data.readline()
        data.close()
        if (title == name_field ):
            print("Файл справочника существует- Dictionary.txt")
        else:
            data = open(file_name,'w', encoding='utf-8')
            data.writelines(name_field)
            data.close()
            print("Файл справочника неверного формата\nCоздан пустой справочник - Dictionary.txt ")
            return
    else:
        print("Файл отсутствует и будет создан")
        data = open(old_filename,'w', encoding='utf-8')
        data.writelines(name_field)
        data.close()
        return


    return

import os.path
from os import path
# import time

import msvcrt


name_field = ("Фамилия Имя Отчество Номер_телефона\n")
file_name = "Dictionary.txt"

test_file_dictionary(name_field,file_name)   
user_command = 1
while user_command != "0":
    print("\nДопустимые команды:\n Завершить работу -- 0 \n Распечатать справочник -- 1 \n Добавить контакт -- 2 \n Найти контакт по фамилии -- 3 \n Найти контакт по имени -- 4 \n Найти контакт по номеру телефона -- 5 ")
    print(" Переписать контакт в новый файл -- 6\n Переписать контакт в имеющийся файл --7\n")
    user_command = input("Введите_команду: ")
    if user_command == "0":
        print("\n Программа завершила работу\n")
        break
    if user_command == "1":
        # печать справочника
        print_dictionary(file_name)
    elif user_command == "2":
        # добавить контакт
        add_contact(file_name)
    elif user_command == "3":
        # найти по фамилии
        print(f"Поиск контакта\nФамилия:", end=" ")
        find_user(file_name,0)
    elif user_command == "4":
        # найти по имени
        print(f"Поиск контакта\nИмя:", end=" ")
        find_user(file_name,1)
    elif user_command == "5":
        # найти по телефону
        print(f"Поиск контакта\nТелефон:", end=" ")
        find_user(file_name,3)
    elif user_command == "6":
        rewrite_contact(file_name)
    elif user_command == "7":
        rewrite_in_oldfile(file_name)
    else:
        print("Недопустимая команда\nНажмите клавишу")
        msvcrt.getch()
