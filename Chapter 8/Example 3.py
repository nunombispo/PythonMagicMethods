# Chapter 8 - Example 3


class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __hash__(self):
        return hash((self.id, self.name))


customer1 = Customer(1, 'Alice')
customer2 = Customer(2, 'Bob')
customer3 = Customer(1, 'Alice')
print(hash(customer1))
print(hash(customer2))
print(hash(customer3))

# Output:
# 3159711117978889722
# 4312602249073901271
# 3159711117978889722
