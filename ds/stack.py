class Stack:
    def __init__(self):
        self._data = []
    def push(self, item):
        self._data.append(item)
    def pop(self):
        return self._data.pop()
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return len(self._data)
    def __str__(self):
        return str(self._data)
    __repr__ = __str__
