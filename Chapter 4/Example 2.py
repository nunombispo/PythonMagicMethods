# Chapter 4 - Example 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() == other.area()

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


rectangle1 = Rectangle(2, 3)
rectangle2 = Rectangle(3, 4)
rectangle3 = Rectangle(2, 3)
print(rectangle1 == rectangle2)
print(rectangle1 == rectangle3)
print(rectangle1 < rectangle2)
print(rectangle1 < rectangle3)

# Output:
# False
# True
# True
# False
