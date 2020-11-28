class Stack(object):
    def __init__(self):
        self.array = []
    
    def __len__(self):
        return len(self.array)
    
    def pull(self):
        return self.array.pop()
    
    def push(self, item):
        self.array.append(item)