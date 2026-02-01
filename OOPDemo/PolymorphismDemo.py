
# Method Overriding ( overwrite )

class Car:
    def start(self):
        print("car start  ")

    def stop(self):
        print("car stops ")

class BMW(Car):
    def speed(self):
        print("BMD speeds really fast")

    def start(self,brand):
        print("BMW start  ")

b1 = BMW()
b1.start("Toyoto")

c1 = Car()
c1.start()



'''
print(10+30)
print("10"+"30")
'''
