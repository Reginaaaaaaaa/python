class Person():
    def __init__(self, name, age, height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight




class Student(Person):
    def __init__(self, name, age, height, weight,study):
        super().__init__(name, age, height, weight,study)


class Name():
    def __init__(self, name):
        self.name = name
    def get_name(self):
        print('getter')
        return self.__hidden_name
    def set_name(self,name):
        print('setter')
        self.__hidden_name = name
    name = property(get_name, set_name)


n  =  Name('Dimas')
n.name = 'Sonya'

print(n.name)



class Counter():
    __counter_value = 0
    def count(self):
        self.__counter_value+=1
    def counter_zero(self):
        self.__counter_value=0
    def get(self):
        return self.__counter_value
    def set(self, n):
        self.__counter_value=n
    count = property(get,set)

c = Counter()
c.count
print(c.get())


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Parent(Person):
    def __init__(self, name, age, hair, eyes):
        super().__init__(name, age)
        self.hair = hair
        self.eyes = eyes

import random
#class Children(Person):
 #   def __init__(self, name, age, p1, p2):
  #      super().__init__(name, age)
   #     hair_1,eyes_1 = p1.hair,p1.eyes
    #    hair_2,eyes_2 = p2.hair,p2.eyes
     #   self.hair  = random.choice([hair_1, hair_2])
      #  self.eyes = random.choice([eyes_1, eyes_2])

#p1 = Parent('James', 34, 'brown', 'blue')
#p2 = Parent('Molly', 31, 'black', 'green')

#c = Children('Sonya', 11, p1, p2)

#print(c.eyes, c.hair)



    
class Car ():
    def __init__(self, speed, name, mark):
        self.speed = speed
        self.name = name
        self.mark = mark

c1 = Car(23,'L987KJ','Lenovo')
c2 = Car(54, 'L0989DF','DFGH')
pos1 = 0
pos2 =0
while True:
    if (pos1+c1.speed) > (pos2+c.speed):
        print('Win ',c1.mark,c1.name)
    else:
        print('Win ', c2.mark, c2.name)



        







