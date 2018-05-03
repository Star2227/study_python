class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_car(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

my_new_car = Car("aodi","a4",2016)
print(my_new_car.get_car())
