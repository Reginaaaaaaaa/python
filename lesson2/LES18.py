l = [0, 1]
try:
    l[2]
except IndexError as err: #err -  переменная чтобы использовать
    print('Неверный индекс', err)
else:
    print('все окей')
finally:
    print('В любом случае') #в любом случае что-тот нужно вывести
#else  если ошибка не вылетела


#TypeError неправильный тип данных '1' + 1
# IndexError индекса не существует
# ZeroDivisionError делить на ноль
# объявлен список и через цикл while брать input и выводить значения из списка q- выход с indexerror



s = '2'
r = 1

try:
    m = s+r
except TypeError as err:
    print('ты чего наделал', err)
else:
    print('молодец')


d = 0

try:
    n = r/d
except ZeroDivisionError as err:
    print('в школе не учился??', err)
else:
    print('умничка')


