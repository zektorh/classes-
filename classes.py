class Users: 
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    def printname(self):
        print(f"hello {self.name}")

class user1(Users):
    def __init__(self, name, lastname, number):
        super().__init__(name, lastname)
        self.number = number

class user2(Users):
    def __init__(self, name, lastname, kodemelli):
        super().__init__(name, lastname)
        self.kodemelli = kodemelli

u = user1("hossein", "azimi", "0239482")

u.printname() # hello hossein