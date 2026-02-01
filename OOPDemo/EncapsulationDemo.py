class Person:
    name = "Ajith"
    _bank_balance=70000000
    __secret = "abcd"

    def get_details(self):
        print(self.name)
        print(self._bank_balance)
        print(self.__secret)

class Engineer(Person):
    pass




'''
p1 = Person()
print(p1.name)
print(p1._bank_balance)
p1.get_details()
'''

e1 = Engineer()
print(e1.name)
print(e1._bank_balance)
e1.get_details()


