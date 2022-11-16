class MyCircularQueue:
    def __init__(self,limit):
        self.limit = limit
        self.right = self.right = -1 
        self.array = [] 

    def Front(self):
        if(self.array == []):
            return -1 
        return self.array[0] 

    def Rear(self): 
        if(self.array == []):
            return -1 
        return self.array[-1] 

    def enQueue(self,n):
        if(len(self.array)<self.limit):
            self.array.append(n) 
            return True 
        return False 

    def deQueue(self):
        if(self.array == []):
            return False 
        self.array.pop(0) 
        return True 

    def isEmpty(self):
        return self.array == [] 
    
    def isFull(self):
        return len(self.array) == self.limit


q = MyCircularQueue(3) 
print(q.enQueue(1))
print(q.enQueue(2)) 
print(q.enQueue(3))
print(q.enQueue(4)) 
print(q.Rear()) 
print(q.isFull()) 
print(q.deQueue()) 
print(q.enQueue(4))
print(q.Rear()) 
