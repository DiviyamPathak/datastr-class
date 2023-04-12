class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if self.is_empty():
            return None

        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def get_size(self):
        return len(self.stack1) + len(self.stack2)

divbyam = Queue()
divbyam.enqueue(4)
divbyam.enqueue(2)
divbyam.enqueue(3)
print(divbyam.is_empty() ,divbyam.get_size() , divbyam.dequeue())