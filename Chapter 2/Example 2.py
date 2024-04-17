# Chapter 2 - Example 2

class Date:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"  # Useful for debugging.

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"  # User-friendly string format.


date = Date(2020, 1, 1)
print(date)
print(repr(date))

# Output:
# 2020-1-1
# Date(2020, 1, 1)
