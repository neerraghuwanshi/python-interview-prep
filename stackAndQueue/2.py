# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.

from stackAndQueue.stack import Stack


class StackMin(Stack):
    def __init__(self):
        super().__init__()
        self.mins = Stack()
        
    def push(self, value):
        super.push(value)
        if not self.mins or value <= self.mins:
            self.mins.push(value)
            
    def pop(self, value):
        value = super.pop()
        if value == self.minimum:
            self.mins.pop()
        return value
        
    def minimum(self):
        self.mins.peek()