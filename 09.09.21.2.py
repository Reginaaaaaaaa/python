from random import randrange


def gen_name(num):
    i=1
    while i<num:
        s= ''
        for x in range(0, 3):
            s += chr(randrange(65, 91))
            s += chr(randrange(97, 123)) * 4


            if x < 4:
               s += ' ' 
        yield s
        i += 1



    
ranger= gen_name(3)
result = [x for x in ranger]
print(result)

