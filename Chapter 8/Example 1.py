# Chapter 8 - Example 1


class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


add_five = Adder(5)
print(add_five(10))

# Output: 15
