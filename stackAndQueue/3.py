# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a functionpopAt(int index) which  performs a pop operation on a specific sub-stack.


from stackAndQueue.stack import Stack


class SetOfStacks:
    def __init__(self, stackCapacity):
        self.stacks = [Stack()]
        self.stackCapacity = stackCapacity
        
    def push(self, value):
        if len(self.stacks[-1]) == self.stackCapacity:
            self.stacks.append(Stack())
        self.stacks[-1].push(value)
    
    def pop(self):
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
            self.pop()
        else:
            return self.stacks[-1].pop()
            
    def popAtIndex(self, index):
        if len(self.stacks[index]) == 1 and index < len(self.stacks):
            return self.stacks.pop(index)
        else:
            return self.stacks[index].pop()
        
    def isEmpty(self):
        return len(self.stacks) == 0
    
    def printStack(self):
        for item in self.stacks:
            for i in item.array:
                print(i)
            print('------')