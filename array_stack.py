class ArrayStack:
    """A stack made with a fixed-size Python list."""

    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.capacity = capacity
        self.items = [None] * capacity
        self.top_index = -1

    def is_empty(self):
        return self.top_index == -1

    def is_full(self):
        return self.top_index == self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack overflow: the stack is full.")
        self.top_index += 1
        self.items[self.top_index] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: the stack is empty.")
        item = self.items[self.top_index]
        self.items[self.top_index] = None
        self.top_index -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek: the stack is empty.")
        return self.items[self.top_index]

    def __str__(self):
        if self.is_empty():
            return "[] (empty)"
        return str(self.items[:self.top_index + 1])
