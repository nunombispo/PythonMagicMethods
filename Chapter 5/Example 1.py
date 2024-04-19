# Chapter 5 - Example 1


class ProtectedAttributes:
    def __init__(self, name):
        self._name = name

    def __getattr__(self, item):
        if item == "name":
            return self._name
        raise AttributeError(f"{self.__class__.__name__} object has no attribute '{item}'")

    def __setattr__(self, key, value):
        if key == "name" and hasattr(self, '_name'):
            raise AttributeError("name attribute is read-only")
        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == "_name":
            raise AttributeError("Cannot delete name attribute")
        super().__delattr__(item)


protected = ProtectedAttributes("Alice")
print(protected.name)
protected.name = "Bob"
del protected._name

# Output:
# Alice
# AttributeError: name attribute is read-only
# AttributeError: Cannot delete name attribute
