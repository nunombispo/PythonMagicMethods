# Chapter 1 - Example 1

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"


car = Car("Toyota", "Corolla")
print(car)

# Output:
# Toyota Corolla
