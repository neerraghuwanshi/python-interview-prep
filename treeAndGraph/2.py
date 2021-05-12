# Given a sorted (increasing order) array with unique integer elements, write an algo­rithm to create a binary search tree with minimal height.

from math import ceil


class Node2:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self, root=None):
        self.root = root
        
    def printTree(self, node):
        if node:    
            self.printTree(node.left)
            print(node.value)
            self.printTree(node.right)
        
    def findLeaf(self, start):
        A = [start]
        while A:
            node = A.pop(0)
            if node.left and node.right:
                if node.left:
                    A.append(node.left)
                if node.right:
                    A.append(node.right)
            else:
                return node
        
    def appendChild(self, value):
        newNode = Node2(value)
        if not self.root:
            self.root = newNode
        else:
            leafNode = self.findLeaf(self.root)
            if not leafNode.left:
                leafNode.left = newNode
            else:
                leafNode.right = newNode


def addChild(array, start, end):
    mid = (start + end) // 2
    if end < start:
        return None
    node = Node2(array[mid])
    node.left = addChild(array, start, mid-1)
    node.right = addChild(array, mid+1, end)
    return node


def minimalTree(A, left, right):
    if not left > right:
        mid = (left + right) // 2
        node = Node(A[mid])
        node.left = minimalTree(A, left, mid-1)
        node.right = minimalTree(A, mid+1, right)
        return node
            
            
A = [1, 2, 3]        


tree = minimalTree(A)
tree.printTree(tree.root)
print('---')