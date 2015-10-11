class Queue:
    def __init__(self):
        self._data = []
    def enqueue(self, item):
        self._data.insert(0, item)
    def dequeue(self):
        return self._data.pop()
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return len(self._data)
    def __str__(self):
        return str(self._data)
    __repr__ = __str__
