import sqlite3

print('Уровень 1-Легкий-')
connection = sqlite3.connect(database='D:\\question.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM quizQ WHERE id=1;')
print(cursor.fetchall())
cursor.execute('SELECT * FROM answerQ ')
print(cursor.fetchall())

answ = str(input('Ваш ответ: '))


if answ ==str(1):
    print('Правильно!')
else:
    print('Неправильно!')

cursor.execute('SELECT * FROM quizQ WHERE id=2;')
print(cursor.fetchall())
cursor.execute('SELECT * FROM quizQ2')
print(cursor.fetchall())

answ2 = str(input('Ваш ответ: '))

if answ2 ==str(3):
    print('Правильно!')
else:
    print('Неправильно!')

cursor.execute('SELECT * FROM quizQ WHERE id=3;')
print(cursor.fetchall())
cursor.execute('SELECT * FROM answ3')
print(cursor.fetchall())

answ3 = str(input('Ваш ответ: '))

if answ3 ==str(4):
    print('Правильно!')
else:
    print('Неправильно!')




