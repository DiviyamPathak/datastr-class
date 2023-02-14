class LlS:
    # class to implement a linked list based stack 
    class Node:
     # single node maker 
        def __init__(self,elem,nextnd):
            self.data = elem
            self.next = nextnd
    
    def __init__(self):
        self.head = None
        self.size = 0

    def sizeof(self) :
        #size 
        return self.size
    def push(self,datapush):
        new = self.Node(datapush,None)
       
        if self.size > 0:
            new.next = self.head
        self.head = new
        self.size += 1
    def top(self):
        if self.size == 0 :
            raise Exception("no elemenets")
        return self.head.data

    def pop(self):
        if self.size == 0:
            raise Exception("Stack is empty")
        self.size -= 1
        delenode = self.head
        self.head = self.head.next
        return delenode.data
    # def pop(self):
    #     if self.size == 0:
    #         raise Empty("no elements to pop")
    #     self.size -= 1
    #     delenode = self.head

    #     self.head = self.head.next
        
    #     return delenode



ned = LlS()
ned.push(43)
ned.push(3)
ned.push(10)
ned.push(18)

print("size",ned.sizeof())
print("popped",ned.pop())
print("size",ned.sizeof())
print("top", ned.top() )