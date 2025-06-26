class Public:
    def __init__(self):
        self.name = "sakthi"  
        self.age=20

    def display_name(self):
        print(self.name,self.age)  

obj = Public()
obj.display_name()  
 

class Protected:
    def __init__(self):
        self._food="Biriyani" 
        self._juice="mango"


class Subclass(Protected):
    def list_item (self):
        print(self._food) 
        print(self._juice) 

obj = Subclass()
obj.list_item()        


class Private:
    def __init__(self):
        self.__price= 50
    
    def price(self):
        return self.__price 

obj = Private()
print(obj.price())
