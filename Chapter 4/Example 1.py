# Chapter 4 - Example 1


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"


product1 = Product("Apple", 1.0)
product2 = Product("Banana", 2.0)
product3 = Product("Apple", 1.0)
print(product1 == product2)
print(product1 == product3)
print(product1 < product2)
print(product1 < product3)

# Output:
# False
# True
# True
# False
