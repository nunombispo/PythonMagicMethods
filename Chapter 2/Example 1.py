# Chapter 2 - Example 1

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point = Point(3, 4)
print(point)

# Output:
# Point(3, 4)
