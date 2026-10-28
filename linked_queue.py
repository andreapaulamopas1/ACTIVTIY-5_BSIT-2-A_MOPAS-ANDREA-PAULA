class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    """A queue made with linked nodes and head/tail references."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def is_full(self):
        # A linked queue has no fixed capacity.
        return False

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: the queue is empty.")
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.head is None:
            self.tail = None
        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Cannot peek: the queue is empty.")
        return self.head.data

    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return str(values) + (" (front to rear)" if values else " (empty)")
