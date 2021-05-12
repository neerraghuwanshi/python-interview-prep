class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        

class Tree:
    def __init__(self, root=None):
        self.root = root