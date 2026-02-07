class Vehicle:

    '''
    def __init__(self):
        print("I am 1st constrcutor...")


    def __init__(self,brand_name):
        print("I am 2nd constructor...")
        self.brand_name = brand_name
    '''

    def __init__(self, brand_name="unknown",vehicle_type="unknown",country_origin="unknown"):
        self.brand_name = brand_name
        self.vehicle_type = vehicle_type
        self.country_origin = country_origin



    def print_all_parameters(self):
        print("Brand name : ",self.brand_name)
        print("vehicle type  : ", self.vehicle_type)
        print("country of origin name : ", self.country_origin)


    def start(self):
        print("Vehcile started...")

    def stop(self):
        print("Vehcile stopped...")

#v1 = Vehicle()
#v1.start()
#v1.stop()
#print("Btrand name is :",v1.brand_name)

# Creating objects with dofferent parameters
#v1 = Vehicle()
#v1.print_all_parameters()

#v2 = Vehicle("Maruti","car","India")
#v2.print_all_parameters()

v3 = Vehicle(brand_name="Maruti",vehicle_type = "car")
v3.print_all_parameters()