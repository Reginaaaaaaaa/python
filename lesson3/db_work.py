import sqlite3
from os import listdir
from os.path import isfile, join

def showall():
    sqliteConnection = sqlite3.connect('db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = (cursor.fetchall())
    [[print(element) for element in row] for row in rows]
    sqliteConnection.close()
    print('Connection is closed now')
def edit(id, brand, value):
    sqliteConnection = sqlite3.connect('D://Databases//{}'.format(p))
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    #sqlite_update_query = """Update middle set id = %d and brand = "%s" where value = "%s\""""
    sqlite_update_query = """Update middle set value = "{:2}", brand = "{:1}" where id = {:0}""".format(value, brand, id)
    columnValues = value, brand, id
    cursor.execute(sqlite_update_query)
    sqliteConnection.commit()
    print("Updated successfully")
    sqliteConnection.commit()
    cursor.close()
def readSqliteTable():
    try:
        print(p)
        sqliteConnection = sqlite3.connect('D://Databases//{}'.format(p))
        cursor = sqliteConnection.cursor()

        sqlite_select_query = """SELECT * from middle"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        for row in records:
            print("ID: ", row[0])
            print("Brand: ", row[1])
            print("Value: ", row[2])
            print("\n")

        cursor.close()
        sqliteConnection.close()

    except sqlite3.Error as error:
        print("Failed to read data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

while True:
    print('a.Выбрать БД для работы', '\n2.Выйти')
    user_a = input()
    if user_a == 2:
        print('Sayonara!')
        quit()
    break

def call(user_a):
    if user_a == 'a':
        print('Список БД: ')
        onlyfiles = [f for f in listdir("D://Databases//") if
                             isfile(join("D://Databases//", f))]
        [print(i + 1, ':', onlyfiles) for i, onlyfiles in zip(range(len(onlyfiles)), onlyfiles)]
        print('Нажмите q для выхода')
        global p
        p = input('Введите имя БД: ')
        if p == 'q':
            print('До свидания')
            quit()

call(user_a)

while True:
        print('1.Редактирование','\n2.Отображение','\na.Другая БД','\n4.Выйти')
        user_a = input()
        if user_a == '1':
            print('Enter ID:')
            id = int(input('Your ID: '))
            print('Enter Brand: ')
            brand = input('Your Brand: ')
            print('Enter Value:')
            value = input('Your Value: ')
            edit(id, brand, value)
            readSqliteTable()
        if user_a == '2':
            readSqliteTable()
        if user_a == 'a':
            call(user_a)
        if user_a == '4':
            print('Thanks for using us!')
            quit()



#onlyfiles = [f for f in listdir("/home/sirius/homework/1910/Databases/") if isfile(join("/home/sirius/homework/1910/Databases/", f))]
#[print(i + 1, ':', onlyfiles) for i, onlyfiles in zip(range(len(onlyfiles)), onlyfiles)]



