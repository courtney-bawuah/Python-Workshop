#!/Users/courtney.bawuah/.pyenv/shims/python

class Car:
    def __init__(self, colour):
        self.colour = colour

    def set_Colour(self, colour):
        self.colour = colour

my_first_car = Car("red")
my_second_car = Car("blue")

print(my_first_car.colour)
print(my_second_car.colour)

my_first_car.set_Colour("purple")
print(my_first_car.colour)