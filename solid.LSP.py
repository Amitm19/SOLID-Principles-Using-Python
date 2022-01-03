class car():
    def __init__(self,type):
        self.type = type
        self.car_properties = {}

    def set_properties(self,color,gear,capacity):
        self.car_properties = {"color": color,"gear":gear, "Capacity": capacity}

    def get_properties(self):
        return self.car_properties

class petrol_car(car):
    def __init__(self,type):
        self.type = type
        self.car_properties = {}

car = car("SUV")
car.set_properties("Red","Auto",6)

petrol_car = petrol_car("Sedan")
petrol_car.set_properties("Blue","Manual",4)

cars = [car , petrol_car]

def find_red_cars(cars):
    red_cars = 0
    for car in cars:
        if car.get_properties()['color'] == "Red":
            red_cars += 1
    print(f'Number of Red Cars = {red_cars}')
find_red_cars(cars)
