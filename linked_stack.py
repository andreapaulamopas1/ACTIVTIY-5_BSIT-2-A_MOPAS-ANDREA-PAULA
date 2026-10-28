class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    """A stack made with linked nodes. It has no fixed capacity."""

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def is_full(self):
        # A linked stack has no fixed capacity.
        return False

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: the stack is empty.")
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek: the stack is empty.")
        return self.head.data

    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return str(values) + (" (top first)" if values else " (empty)")
