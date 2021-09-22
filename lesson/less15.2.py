list_ = [1,1, 2, 2, 3, 4,]  # список с уникальными значениями

def unique(list_):
    a= set(list_)
    s = list(a)
    return s

print (unique(list_))


list1 = [1, 2, 3, 4] # список с общими значениями
list2 = [1, 5, 3, 6]

def rer(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    b = set1.intersection(set2)
    d = list(b)
    return d
print(rer(list1, list2))


















