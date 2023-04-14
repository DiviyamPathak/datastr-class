class cdll:
    
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
    #     self.prev = None
    def insert_values(self, data_list):
        self.head = None
        self.tail = None
        for data in data_list:
            self.add_node(data)

    
    def add_node(self, data):
        new_node = self.Node(data)
        if self.is_empty():
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            last_node = self.head.prev
            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.head
            self.head.prev = new_node

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_after_value(self, data):
        new_node = self.Node(data)
        if self.is_empty():
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            last_node = self.head.prev
            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.head
            self.head.prev = new_node

    def remove_by_value(self, data):
        if self.is_empty():
            return
        curr_node = self.head
        while True:
            if curr_node.data == data:
                if curr_node == self.head:
                    self.head = curr_node.next
                prev_node = curr_node.prev
                prev_node.next = curr_node.next
                curr_node.next.prev = prev_node
                del curr_node
                return
            curr_node = curr_node.next
            if curr_node == self.head:
                return

    def print_forward(self):
        if self.is_empty():
            return
        curr_node = self.head
        while True:
            print(curr_node.data, end=' ')
            curr_node = curr_node.next
            if curr_node == self.head:
                break
        print()

    def print_backward(self):
        if self.is_empty():
            return
        curr_node = self.head.prev
        while True:
            print(curr_node.data, end=' ')
            curr_node = curr_node.prev
            if curr_node == self.head.prev:
                break
        print()

    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None


    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_after_value(self, data_after, data_to_insert): 

        # Search for first occurance of data_after value in linked list 
        if self.head is None:
            return
        node = self.head
        while node is not None and node.data != data_after:
            node = node.next
        if node is None:
            return
        new_node = self.Node(data_to_insert)
        new_node.next = node.next
        new_node.prev = node
        if node.next is None:
            self.tail = new_node
        else:
            node.next.prev = new_node
        node.next = new_node
        

        # Now insert data_to_insert after data_after node 

    def remove_by_value(self, data):
        # Find the node with the given data
        node = self.head
        while node is not None and node.data != data:
            node = node.next

        # If the node wasn't found, return
        if node is None:
            return

        # If the node is the head, update the head pointer
        if node == self.head:
            self.head = node.next

        # If the node is the tail, update the tail pointer
        if node == self.tail:
            self.tail = node.prev

        # Update the next and previous pointers of the nodes surrounding the removed node
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        # Clear the next and previous pointers of the removed node
        node.prev = None
        node.next = None


        

    # def print_forward(self): 

    #     # This method prints list in forward direction. Use node.next. Use a print statement to print the nodes in forward direction starting from the first node to the last node. 

    # def print_backward(self): 

    #     # Print linked list in reverse direction. Use node.prev for this. Use a print statement to print the nodes



LL = cdll() 

LL.insert_values(["Red","Yellow","Purple","Orange"]) 

print(getattr((LL),"Node")) 

LL.insert_after_value("Yellow","Blue") # insert Blue after Yellow 

print(getattr((LL),"Node")) 

LL.remove_by_value("orange") # remove Orange from linked list 

print(getattr((LL),"Node")) 

LL.remove_by_value("Green") 

print(getattr((LL),"Node")) 

LL.remove_by_value("Red") 

LL.remove_by_value("Yellow") 

# LL.remove_by_value("Blue") 

LL.remove_by_value("Purple") 

print(getattr((LL),"Node")) 

LL.print_forward() 

LL.print_backward() 