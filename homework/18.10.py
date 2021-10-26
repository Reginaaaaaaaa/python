import random
import sqlite3

connection = sqlite3.connect('db')
cursor = connection.cursor()


def format(level):
    # level = 1
    cursor.execute('SELECT COUNT(*) FROM level_%d' % level)
    fa = cursor.fetchall()
    d = random.randint(1, fa[0][0])
    cursor.execute('SELECT question FROM level_%d WHERE id=%d;' % (level, d))
    # cursor.execute('SELECT question FROM level_1 WHERE id=' + str(d) +';')
    row = (cursor.fetchall())
    print(row[0][0])
    cursor.execute('SELECT answer1, answer2, answer3, answer4 FROM level_%d WHERE id=%d;' % (level, d))
    answers = (cursor.fetchall())[0]
    [print(i + 1, ':', answer) for i, answer in zip(range(len(answers)), answers)]
    cursor.execute('SELECT question, answer1, answer2, answer3, answer4, right_answer FROM level_%d WHERE id=%d;' % (level, d))
    list_ = (cursor.fetchall())
    q, a1, a2, a3, a4, ra = list_[0]
    # print(list_)
    try:
        user_a = int(input())
    except Exception as err:
        print('Альберт Андреевич, не надо так делать!', err)
        quit()
    if user_a == 1:
        user_a = a1
    if user_a == 2:
        user_a = a2
    if user_a == 3:
        user_a = a3
    if user_a == 4:
        user_a = a4
    if user_a == ra:
        print('Atari, Oni-chan! To the next question~~~')
        level += 1
    else:
        print('You can do better, Oni-chan!')
        quit()

    return level

level = 1
while level < 6:
    level = format(level)
else:
    print("*** Winner winner chicken dinner! ***")
connection.commit()
cursor.close()
connection.close()