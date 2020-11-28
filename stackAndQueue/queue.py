class Queue(object):
    def __init__(self):
        self.array = []
    
    def __len__(self):
        return len(self.array)
    
    def deque(self):
        return self.array.pop(0)
    
    def enque(self, item):
        self.array.append(item)