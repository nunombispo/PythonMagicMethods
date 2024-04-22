# Chapter 6 - Example 1


class CustomList:
    def __init__(self):
        self._storage = []

    def __len__(self):
        return len(self._storage)

    def __getitem__(self, index):
        return self._storage[index]

    def __setitem__(self, index, value):
        if index >= len(self._storage):
            self._storage.extend([None]*(index + 1 - len(self._storage)))
        self._storage[index] = value

    def __delitem__(self, index):
        del self._storage[index]

    def __repr__(self):
        return f"CustomList({self._storage})"


custom_list = CustomList()
custom_list[0] = 1
custom_list[1] = 2
custom_list[2] = 3
print(custom_list)
print(len(custom_list))
del custom_list[1]
print(custom_list)
print(len(custom_list))

# Output:
# CustomList([1, 2, 3])
# 3
# CustomList([1, 3])
# 2

