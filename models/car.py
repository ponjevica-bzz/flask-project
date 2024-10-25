class Car:
    def __init__(self, car_id, make, model, year):
        # A1G: Pure function that initializes a car object without side effects
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        # A1G: Another pure function to represent the car as a string
        return f"{self.make} {self.model} ({self.year})"
