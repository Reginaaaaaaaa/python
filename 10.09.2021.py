import string
s = string.ascii_lowercase

l = [c for c in s]

def f(l):
    for d in l:
        print(d)


def f2(l):
    i=0
    while i<len(l):
        print(l[i])
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

f2_dec(l)