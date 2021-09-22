import string
s = string.ascii_lowercase
a = [c for c in s]

def f(a):
    for d in a:
        print(d)


def f2(a):
    i=0
    while i<len(a):
        print(a[i])
        i+=1


def dec(leng):
    def new_leng(*args,**kwargs):
        print('Running function: ', leng.__name__)
        print('Positional arguments are: ', args)
        print('Keyword arguments are: ', kwargs)
        result = leng(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_leng

f2_dec = dec(f2)
f2_dec(a)