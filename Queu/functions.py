class DSAqueue():
    defaultcapacity = 100    

    def __init__(self, maxcapacity=None):
        if maxcapacity is None:
            maxcapacity = DSAsqueue.defaultcapacity
        self.queue0 = [0] * maxcapacity  # Allocate stack array 
        self.count = 0        

    def getCount(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.stack)

    def push(self, value):
        if self.isFull():
            raise Exception("Stack is full. Cannot push value.")
        else:
            self.stack[self.count] = value
            self.count += 1
    
    def top(self):
        if self.isEmpty():
            raise Exception("Stack is empty. Nothing to see.") 
        else:
            return self.stack[self.count-1] 

    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop ftom an empty stack")        
        topVal = self.top()
        self.count -= 1
        return topVal