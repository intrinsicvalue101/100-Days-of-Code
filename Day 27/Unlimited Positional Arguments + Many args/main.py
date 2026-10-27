# TODO: unlimited args, a function can accept any number of arguments
#  used when you want to refer to positional arguments
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(3,4,5))

# TODO: many keyword arguments
#  used when you want to refer to args by name
def calculate(n, **kwargs): # kwargs = optional keyword args
    print(kwargs) # creates dictionary
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5) # kwargs is dictionary of add, multiply values

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)