file = input('Введите файл: ')
try:
    g = int(input('Балл: '))
except Exception as err:
    print('Ошибка! Введите целое число ', err)
    quit()
try:
    f = open(file, 'r')
except Exception as err:
    print('Файл не найден', err)
    quit()

lines = f.readlines()
for line in lines:
    p = line.split()
    b = p[-1]
    try:
        c = int(b)
    except Exception as err:
        print('В файле должны быть указаны целые числа!', err)
    if c <= g:
        print(p [0:2], b)