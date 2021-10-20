#Написать рекурсию

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

def ord(n):
    if n < 10:
        return [n]
    return ord(n // 10)+[n % 10]

print(ord(234))