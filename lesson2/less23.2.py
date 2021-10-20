import random

class Car ():
    def __init__(self, speed, name, mark):
        self.speed = speed
        self.name = name
        self.mark = mark

s1 = random.randint(1,100)
s2 = random.randint(1,100)

c1 = Car(s1,'L987KJ','Ferrari')
c2 = Car(s2, 'L0989DF','Lada')
pos1 = 0
pos2 =0
while True:
    if (pos1+c1.speed) > (pos2+c2.speed):
        print('Win ',c1.mark,c1.name)
        break
    else:
        print('Win ', c2.mark, c2.name)
        break







