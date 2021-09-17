def validate_number(a):
    if len(a) !=16:
        return False
    if a[0:3] !='+7-':
        return False
    if a[6] !='-' or a[10] !='-' or a[13] !='-':
        return False
    ba = a[3:6] + a[7:10] + a[11:13] + a[14:]
    digits = '0123456789'
    for sym in ba:
        if not sym in digits:
            return False
    return True
print(validate_number('+7-930-674-45-27'))


d = {}
p = '+7-930-674-45-27'
def validate_number(p):
    if len(p) != 16:
        return False
    if not p[0:3] == '+7-':
        return False
    if not (p[6] == '-' and p[10] == '-' and p[13] == '-'):
        return False

    actual_phone = p[3:6] + p[7:10] + p[11:13] + p[14:]

    digits = '0123456789'
    for ch in actual_phone:
        if not ch in digits:
            return False
    return True
print(validate_number(p))

def add_to_book(name, phone):
    d[name] = phone
while True:
    name = str(input('введите имя: '))
    if name == 'q':
        print(d)
        break
    phone = str(input('дашь номерок?: '))
    if phone == 'q':
        print(d)
        break
    if validate_number(phone):
        print('все ок')
        add_to_book(name, phone)
        print('новый тел. добавлен')
    else:
        print('это что?? переписывай нормально')