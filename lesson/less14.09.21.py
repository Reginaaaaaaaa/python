#работа со списками

a = {'Adam':2345, 'Sara':4556, 'Jerry':1234}

print(a.keys())
print(a.values())
print(a['Adam'])

a['Adam']= 3456  #изменить значение и добавить Димаса
a['Dimas']=7890

print(a.keys())
print(a.values())

k = 'Dimas'
def vav(a, k):
    if k in a.keys():
        return a[k]
    else:
        return -1


print(vav(a, k))

k = 'Sonya'

def viv(a, k):
    return a.get(k, -1)  #проверяем есть ли там Димас
  
print(vav(a, k)) #Димаса нет((



m = {'German':5678, 'Masha':4523}  #Создаем список и объединяем с прошлым

a.update(m)

print(a)

s = 'Thanks, Jhon, my wife is okay'

'[]' = int(input())

def counter(s):
    z = {}
    if s.count('[]') >= 1:
        z = {s.count('[]')}
    return(z)
print(counter(s))



  







