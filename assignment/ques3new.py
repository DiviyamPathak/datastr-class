class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.front = -1
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def add_front(self, value):
        if self.is_full():
            return False

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1) % self.capacity

        self.arr[self.front] = value
        self.size += 1
        return True

    def add_rear(self, value):
        if self.is_full():
            return False

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.arr[self.rear] = value
        self.size += 1
        return True

    def remove_front(self):
        if self.is_empty():
            return None

        value = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        if self.size == 0:
            self.front = -1
            self.rear = -1

        return value

    def remove_rear(self):
        if self.is_empty():
            return None

        value = self.arr[self.rear]
        self.arr[self.rear] = None
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1

        if self.size == 0:
            self.front = -1
            self.rear = -1

        return value

    def get_front(self):
        if self.is_empty():
            return None

        return self.arr[self.front]

    def get_rear(self):
        if self.is_empty():
            return None

        return self.arr[self.rear]


hj = Deque(4)

hj.add_front(3)
hj.add_front(4)
hj.add_front(7)
hj.add_front(9)
print(hj.get_front(),hj.get_rear(),hj.is_empty(),hj.is_full())