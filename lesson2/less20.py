#class Name():
 #   def __init__(self, name):
  #      self.name = name
#
#name_2 = Name('Dimas')

#def return_name(self):
 #   return self.name

#name_2.return_name()



class Summator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def return_sum(self):
        return self.a  + self.b

s = Summator(1, 3)
s.return_sum()

print(s.return_sum())

class Car():
    def __init__(self):
        pass
    def what_is_this(self):
        print("I'm a car")

class Pink_car(Car):
    def what_color(self):
        print('pink')

car = Car()
pink_car = Pink_car()
pink_car.what_is_this()

print(pink_car.what_is_this())



class Person():
    def __init__(self, name):
        self.name = name
    def exclaim(self):
        print("I'm a person with name", self.name)
   # def __del__(self):
  #      print('Удален объект', self)

class Student(Person):
    def __init__(self, name):
        self.name = name
    def exclaim(self):
        print("I'm a person with name", self.name, "but i want to sleep more")

p = Person('Dimas')
p.exclaim()
s = Student('Dimas')
s.exclaim()

#p.__del__()

d = isinstance(s, Student) #является ли s объектом класса Student
print(d)

r = issubclass(Student, Person) #является ли потомком
print(r)


class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def get_p(self):
        return (self.w+self.h)*2
    def get_s(self):
        return self.w*self.h

r = Rectangle(3, 5)
r.get_p()

print(r.get_p())
 
import math

class Circle():
    def __init__(self, d, r ):
        self.d = d
        self.r = r
    def get_l(self):
        return math.pi*self.d
    def get_pl(self):
        return math.pi*self.r**2

c = Circle(5, 3)
print(c.get_l())
print(c.get_pl())

class Triangl():
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def get_p(self):
        return self.a+self.b+self.c
    def get_s(self):
        return math.sqrt(self.a*self.h)


t = Triangl(2, 3, 4, 5)
print(t.get_p())
print(t.get_s())





