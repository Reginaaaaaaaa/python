class Reader():
    book = 0
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    def take_book(self):
        if self.book > 2 :
            print('Больше не положено')
        else:
            self.book += 1
        self.book += 1
        return self.book
    def return_book(self):
        return self.book - 1
    

r = Reader('Sara',"Smith", 23)

print(r.take_book())
print(r.take_book())
print(r.return_book())

