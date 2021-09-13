from random import choice
import string

def create (num):
    result = ''
    for i in range (num):
        result += choice(string.ascii_letters)
    return result

l = []
def lenth(s):
    big = 0
    small = 0
    for sum in s:
        if sum.isupper():
            big += 1
        else:
            small += 1
    if big > small:
        return 1
    if small > big:
        return 0
    else:
        return -1

s = create(9)
print('String is: ', s)
print('result is:', lenth(s))