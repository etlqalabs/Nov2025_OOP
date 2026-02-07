class Vehicle:
    def __init__(self,brand_name):
        self.brand_name = brand_name
        print("brand_name :",self.brand_name)
        print("I am Vehicle constuctor")



class Car(Vehicle):
    def __init__(self,brand_name,model):
        super().__init__(brand_name)
        self.model = model
        print("Model :", self.model)
        print("I am Car constuctor")


c = Car("Maruti","Ciaz")


