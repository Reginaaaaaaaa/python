p = '+7-921-076-59-17'
d= {}
name = str(input())


def validate_number(p):  # это номер? ха
    if len(p) != 16:
        return False
    if p[0:3] != '+7-':
        return False
    if p[6] != '-' or p[10] != '-' or p[13] != '-':
        return False
    ap = p[3:6]+p[7:10]+p[11:13]+p[14:]
    digits = '0123456789'
    for sym in ap:
        if not sym in digits:
            return False
    return True

print (validate_number(p))


def add_to_book(name, p):  #номер в словарь
    d[name]= p
    return d

print(add_to_book(name, p))


while type(name) == str:
     name = input("Введите имя ")
     while type(number) == str:
         number = input('Введите номер ')
for i in input():
    if i == 'q':
        break
    