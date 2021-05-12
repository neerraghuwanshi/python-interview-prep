# Describe how you could use a single array to implement three stacks.


class MultiStack:
    def __init__(self, stackSize, numberOfStacks):
        self.stackSize = stackSize
        self.numberOfStacks = numberOfStacks
        self.array = [0 for _ in range(stackSize * numberOfStacks)]
        self.sizes = [0 for _ in range(numberOfStacks)]
        
    def push(self, value, stackIndex):
        if not self.isFull(stackIndex):
            self.sizes[stackIndex] += 1
            self.array[self.topIndex(stackIndex)] = value
    
    def pop(self, stackIndex):
        value = self.array[self.topIndex(stackIndex)]
        self.array[self.topIndex(stackIndex)] = 0
        self.sizes[stackIndex] -= 1
        return value
    
    def isEmpty(self, stackIndex):
        self.sizes[stackIndex] == 0
        
    def isFull(self, stackIndex):
        self.sizes[stackIndex] == self.stackSize
        
    def topIndex(self, stackIndex):
        offset = stackIndex * self.stackSize
        return offset + self.sizes[stackIndex] - 1
    
    def printStack(self):
        print(self.array)