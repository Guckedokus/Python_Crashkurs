class Car ():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.year} {self.make} {self.model} is starting.")
    def brake(self):
        print(f"The {self.year} {self.make} {self.model} is braking.")  
    def turn(self, direction):
        print(f"The {self.year} {self.make} {self.model} is turning {direction}.")
    def park(self):
        print(f"The {self.year} {self.make} {self.model} is parking.")
    def refuel(self):
        print(f"The {self.year} {self.make} {self.model} is refueling.")

my_car = Car("Toyota", "Corolla", 2020)
my_car.start()