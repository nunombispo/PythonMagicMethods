#  Chapter 9 - Example 1


class Registry:
    def __init__(self):
        self._items = {}

    def __getitem__(self, key):
        return self._items.get(key, None)

    def __setitem__(self, key, value):
        self._items[key] = value

    def __repr__(self):
        return f"{self._items}"


registry = Registry()
registry["key1"] = "value1"
registry["key2"] = "value2"
print(registry)

# Output: {'key1': 'value1', 'key2': 'value2'}
