class Stack(object):
    def __init__(self):
        self.array = []
    
    def __len__(self):
        return len(self.array)
    
    def pop(self):
        return self.array.pop()
    
    def push(self, item):
        self.array.append(item)

    def peek(self):
        return self.array[-1]
    
    def is_empty(self):
        return len(self.array) == 0
    
    def print_stack(self):
        for i in range(self.array, -1):
            print(self.array[i])