class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def max_heapify(self, i):
        left = 2*i + 1
        right = 2*i + 2
        largest = i
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)
    
    def build_max_heap(self, arr):
        self.heap = arr[:]
        n = len(arr)
        
        for i in range(n//2 - 1, -1, -1):
            self.max_heapify(i)
    
    def print_heap(self):
        sorted_heap = []
        while len(self.heap) > 0:
            sorted_heap.append(self.heap[0])
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.max_heapify(0)
        return sorted_heap[::-1]

hjp = MaxHeap()
hjp.build_max_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(hjp.print_heap())
hjp.max_heapify(3)
print(hjp.print_heap())