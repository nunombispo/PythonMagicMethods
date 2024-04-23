# Chapter 8 - Example 2


class Container:
    def __dir__(self):
        return ['custom_method1', 'custom_method2']


container = Container()
print(dir(container))

# Output:
# ['custom_method1', 'custom_method2']
