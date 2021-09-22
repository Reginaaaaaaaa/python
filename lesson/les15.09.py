list_ = [1,1,2,2,3,3]  #обявила список
a = set(list_)
print(a)


d = set('aabbccgg') #строку
print(d)

####

set1 = {1,2,3,4,5,6}
set2 = {4, 5, 6, 7, 8, 9}

f = set1.isdisjoint(set2) # фолз если есть одинаковые значения
print(f)

c = set1.issubset(set2) # если все элементы одинаковы то тру
print(c)

g = set1.union(set2) # объединяет множества
print(g)

k = set1.intersection(set2) #общие для обоих значения
print(k)

v = set1.difference(set2) #показывает значения которых нет в сет2
print(v)

e = set1.symmetric_difference(set2) #показывает элементы которых нет друг в друге
print(e)

set1.copy() #копия множества
set3 = set1.copy()
print(set3)

#######


set1.update(set2) #объединяет но не выводит, меняет само множество
print(set1)

set1.intersection_update(set2) #показывает общее, т.к множество уже изменено то вот такой ответ
print(set1)

set1.difference_update(set3) #вычитает одно множество из другого
print(set1)

set1.symmetric_difference_update(set3) #элементы встречающиеся в одном множестве но не вст. в обоих
print(set1)

set1.add(11) # добавляет только один!! элемент в множество
print(set1)

set1.remove(11) # удаляет один элемент, если его там нет то выдает ошибку
print(set1)

set1.discard(4) #удаляет элемент если он там есть
print(set1)

set1.pop() #удаляет первый элемент(не упор, поэтому не знаем какой)
print(set1)

set1.clear() #чистит множество
print(set1)