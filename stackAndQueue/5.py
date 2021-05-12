# Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.


from .stack import Stack


s = Stack()
s.push(2)
s.push(1)
s.push(3)
s.push(3)
s.push(1)
s.push(3)


def sortStack(s):
    tempStack = Stack()
    while not s.is_empty():
        tempStack.push(s.pop())
    while not tempStack.is_empty():
        element = tempStack.pop()
        while not s.is_empty():
            if element > s.peek():
                tempStack.push(s.pop())
            else:
                s.push(element)
                break
        if s.is_empty():
            s.push(element)
            
            
sortStack(s)
s.print_stack()