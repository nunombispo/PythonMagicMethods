# Chapter 7 - Example 2


class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"An exception occurred: {exc_val}")
        # Return True to suppress exceptions, False to propagate them
        return False


with ManagedFile('hello.txt') as file:
    file.write('hello, world!')
    file.write('bye now')
    raise Exception('exception raised')

# Output:
# An exception occurred: exception raised
# Traceback (most recent call last):
#   File "...\Chapter 7\Example 1.py", line 24, in <module>
#     raise Exception('exception raised')
# Exception: exception raised
