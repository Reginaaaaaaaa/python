s= {'key1': 1, 'key2': 3, 'key3': 2}
def sort(s):
    a = sorted(s, key=lambda x:x[1])
    return a
print(sort(s))