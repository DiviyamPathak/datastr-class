class cdll:
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

        # Remove first node that contains data 
        node = self.head
        while node.data != data:
            node = node.next
        if node is None:
            return
        

    def print_forward(self): 

        # This method prints list in forward direction. Use node.next. Use a print statement to print the nodes in forward direction starting from the first node to the last node. 

    def print_backward(self): 

        # Print linked list in reverse direction. Use node.prev for this. Use a print statement to print the nodes



LL = cdll() 

LL.insert_values(["Red","Yellow","Purple","Orange"]) 

LL.print() 

LL.insert_after_value("Yellow","Blue") # insert Blue after Yellow 

LL.print() 

LL.remove_by_value("orange") # remove Orange from linked list 

LL.print() 

LL.remove_by_value("Green") 

LL.print() 

LL.remove_by_value("Red") 

LL.remove_by_value("Yellow") 

LL.remove_by_value("Blue") 

LL.remove_by_value("Purple") 

LL.print() 

LL.print_forward() 

LL.print_backward() 