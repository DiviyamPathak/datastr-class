class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def push_front(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
    
    def push_back(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    def pop_front(self):
        if self.is_empty():
            return None
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return value
    
    def pop_back(self):
        if self.is_empty():
            return None
        value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value
    
    def peek_front(self):
        if self.is_empty():
            return None
        return self.head.value
    
    def peek_back(self):
        if self.is_empty():
            return None
        return self.tail.value
    
    def get_size(self):
        return self.size


fg = Deque()
fg.push_front(3)
fg.push_front(2)
fg.push_front(12)
fg.push_front(352)
print(fg.peek_front(),fg.peek_back(),fg.is_empty(),fg.get_size())