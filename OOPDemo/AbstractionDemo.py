from abc import abstractmethod, ABC

class Vehicle(ABC):

    def start(self):
        print("Vehcile starts..")

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def honk(self):
        pass



class Car(Vehicle):
    def stop(self):
        print("car stops.")

    def honk(self):
        print("Cra honk")

'''
v1 = Vehicle()
v1.start()
'''

c1 = Car()
c1.start()
c1.stop()
c1.honk()