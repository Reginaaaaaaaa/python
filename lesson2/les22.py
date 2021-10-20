#рекурсивная функция

#def f():
#    f()



def f(n):
    print(n)
    if n>0:
        f(n-1)

print(f(10))

def f(n, m):
    print(n)
    if n>m:
        f(n-1, m)
        

print(f(6,5))
    

def fac(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fac(n-1) * n
 
 
print(fac(6))

def f(n, div=1, all_div=[]):
    if div == n:
        all_div.append(div)
        return all_div
    elif div<n:
        if n%div == 0:
            all_div.append(div)
        return f(n,div=div+1,all_div=all_div)
    else:
        print('dfghjk')

print(f(567,div=1,all_div=[]))
    

def g(n):
    s=str(n)
    s[0]
    s[1:]
    return g(n)

print (g(179))
