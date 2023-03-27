class Stackoffixedarray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def push(self, item):
        if self.is_full():
            raise ValueError("Stack is full")
        self.data[self.size] = item
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        self.size -= 1
        item = self.data[self.size]
        self.data[self.size] = None
        return item
    
    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.data[self.size - 1]

obejectstack = Stackoffixedarray(5)

obejectstack.push(7)
obejectstack.push(54)
obejectstack.push(4)
obejectstack.push(0)

