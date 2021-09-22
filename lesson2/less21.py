#private( приватные дв)

class Person():
    def __init__(self, name, age):
            self.__name=name
            self.__age=age
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name = new_name
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        self.__age = new_age
    

st = Person('Dimas', 28)

print(st.get_name())
print(st.get_age())

class Field():
    __pos_hare=0
    __pos_tort=0
    
    def __init__(self, n, m, x):
        self.__step_hare = n
        self.__step_tort = m
        if n<=m:
            print('fghjk')
            return
        self.__pos_hare=n
        self.__pos_tort=m
        self.__lenght=x
    def get_pos_hare(self):
        return self.__pos_hare
    def get_pos_tort(self):
        return self.__pos_tort
    def step(self):
        hare_new_pos = self.__pos_hare+self.__step_hare
        if hare_new_pos>self.__lenght:
            hare_new_pos-=self.__lenght
        self.__pos_hare=hare_new_pos
    def step(self):
        tort_new_pos = self.__pos_tort+self.__step_tort
        if tort_new_pos>self.__lenght:
            tort_new_pos-=self.__lenght
        self.__pos_tort=tort_new_pos


f = Field(5, 2, 11)
i = 0
first_meet = 0

while(i<100):
    f.step()
    i += 1
    if f.get_pos_hare() == f.get_pos_tort():
        print('first meet', i- first_meet)
        first_meet = i
        
import random
class Game():
    def play(self, cards):
        table_card = random.randrange(10)
        winners = []
        i = 0
        for card in cards:
            if (card+table_card)%2 == 0:
                winners += 1
            i +=1
        if len (winners)>0:
            print('Winners: ', winners)
        else:
            print('Defeat')

g = Game()


while True:
    g.play(cards= 1)
    

    
    
    


