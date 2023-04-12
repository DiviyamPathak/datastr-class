from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        self.q1.put(value)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None

        # Move all elements except the last one from q1 to q2
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        # Get the last element from q1
        value = self.q1.get()
        self.size -= 1

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

        return value

    def peek(self):
        if self.is_empty():
            return None

        # Move all elements except the last one from q1 to q2
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        # Get the last element from q1
        value = self.q1.get()

        # Move the element to q2
        self.q2.put(value)

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

        return value

    def get_size(self):
        return self.size


jhui = Stack()
jhui.push(5)
jhui.push(3)
jhui.push(6)
jhui.push(8)
print(jhui.peek(),jhui.get_size(),jhui.is_empty())
jhui.pop()
print(jhui.peek())


