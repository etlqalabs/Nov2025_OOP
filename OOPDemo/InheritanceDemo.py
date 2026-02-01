class Vehicle:
    '''
    def start(self):
        print("Vehicle starts...")
    '''
    def stop(self):
        print("Vehicle stops...")

    def Honk(self):
        print("Vehicle honks...")

class Accessories:
    def mirror(self):
        print("Mirror...")

    def start(self):
        print("Accessory- Vehicle-  starts...")


class Car(Vehicle,Accessories):
    '''
    def start(self):
        print("Car starts...")
    '''

    def stop(self):
        print("Car stops...")


c1 = Car()

c1.start()
