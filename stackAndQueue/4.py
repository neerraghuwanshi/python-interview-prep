# Implement a MyQueue class which implements a queue using two stacks.


from stackAndQueue.stack import Stack


class MyQueue:
    def __init__(self):
        self.queue = Stack()
        self.tempStack = Stack()
        
    def enqueue(self, value):
        if not self.tempStack.is_empty():
            while not self.tempStack.is_empty():
                self.queue.push(self.tempStack.pop())
        self.queue.push(value)
        
    def dequeue(self):
        if self.tempStack.is_empty():
            while not self.queue.is_empty():
                self.tempStack.push(self.queue.pop())
        self.tempStack.pop()
        
    def isEmpty(self):
        return self.queue.is_empty()
    
    def printQueue(self):
        if not self.queue.is_empty():
            while not self.queue.is_empty():
                self.tempStack.push(self.queue.pop())
        while not self.tempStack.is_empty():
            element = self.tempStack.pop()
            self.queue.push(element)
            print(element)