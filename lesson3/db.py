import sqlite3

def show_menu(level):
    if level == 1:
        return '1.New 2.Work with DB 0.Exit'
    else:
        return '1.SELECT 2.UPDATE'

menu_level = 1
connection = None
cursor = None

while True:
    answer= input(show_menu(menu_level))
    if menu_level == 1:
        if answer == '0':
            if connection:
                connection.close()
            if cursor:
                cursor.close()
            break
        elif answer == '2':
            menu_level =2
        elif answer == '1':
            path = input('Введите путь к Бд: ')
            if connection:
                connection.close()
            if cursor:
                cursor.close()
            connection = sqlite3.connect(path)
            cursor = connection.cursor()
    elif menu_level == 2:
        ans = input(show_menu(2))
        if ans == '1':
            select = input('SELECT: ')
            fr = input('FROM: ')
            where = input('WHERE: ')
            if cursor:
                com = 'SELECT %s FROM %s WHERE %s;'%(select, fr, where)
                cursor.execute(com)
                print(cursor.fetchall)
        elif ans == '0':
            menu_level == 1