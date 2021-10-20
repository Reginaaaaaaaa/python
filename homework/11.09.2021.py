import random
import string
s = string.ascii_letters
n = ''
l = [c for c in s]
def cr_str(width):
    l = [random.choice(string.ascii_letters) for i in range(width)]
    s = ''
    for el in l:
        s += el
    return s

def cr_list_str(width, num):
    l = [cr_str(width) for i in range(num) ]
    s = ''
    big = 0
    small = 0
    statb = 0
    stats = 0
    statr = 0
    for el in l:
        s += el
        s += ' '
        for i in el:
            if i.isupper():
                big += 1
            else:
                small += 1
        if big > small:
            statb += 1
            s += '1'
        elif small > big:
            stats += 1
            s += '0'
        else:
            statr += 1
            s += '-1'
        
        s += ' '
    s += '> A ' + str(statb/(statb+stats+statr)*100) + '% '
    s += '> a ' + str(stats/(statb+stats+statr)*100) + '% '
    s += 'a == A ' + str(statr/(statb+stats+statr)*100) + '%'
    return s

print(cr_list_str(8, 8),)