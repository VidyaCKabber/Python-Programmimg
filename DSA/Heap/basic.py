class minHeap:
    
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0
        
    def getParentIndex(self, index):
        return (index - 1) // 2
        
    def getLeftChildIndex(self, index):
        return 2 * index + 1
    
    def getRightChildIndex(self, index):
        return 2 * index + 2
        
    def hasParent(self, index):
        return self.getParentIndex(index) >0
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size # if index of left child is less than size of array ( tree) then True
        
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.index
        
        
    def parent(self, index):
        p = self.getParentIndex(index)
        return self.storage[p]
    
    def LeftChild(self, index):
        l = self.getLeftChildIndex(index) 
        return self.storage[l]
        
    def RightChild(self, index):
        r = self.getRightChildIndex(index)
        return self.storage[r]
        
    def isFull(self):
        return self.capacity == self.size
        
        
    def swap(self, index_1, index_2):
        temp = self.storage[index_1]
        self.storage[index_1] = self.storage[index_2]
        self.storage[index_2] = temp
        
        
    def insert(self, data):
        if(self.isFull()):
            raise("Heap is full")
            
        self.storage[self.size] = data
        self.size += 1
        
    
    
    
