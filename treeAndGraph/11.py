# Random Node: You are implementing a binary tree class from scratch which, in addition to insert, find, and delete, has a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.
import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        
    @property
    def leftSize(self):
        if self.left:
            return self.left.size
        return 0
        
    @property
    def rightSize(self):
        if self.right:
            return self.right.size
        return 0
        

class Tree:
    def __init__(self, root=None):
        self.root = root
        
    def findNode(self, value):
        if self.root:
            A = [self.root]
            while len(A) > 0:
                node = A.pop(0)
                if node.value == value:
                    return node
                if node.left:
                    A.append(node.left)
                if node.right:
                    A.append(node.right)
    
    def findLeaf(self, startNode):
        if self.root:
            A = [startNode]
            while len(A) > 0:
                node = A.pop(0)
                if not node.left or not node.right:
                    return node
                A.append(node.left)
                A.append(node.right)
    
    def incrementParentsSize(self, node):
        if node.parent:
            node.parent.size += 1
            self.incrementParentsSize(node.parent)

    def decrementParentsSize(self, node):
        if node.parent:
            node.parent.size -= 1
            self.decrementParentsSize(node.parent)
        
    def insert(self, value):
        newNode = Node(value)
        if self.root:
            leaf = self.findLeaf(self.root)
            if not leaf.left:
                leaf.left = newNode
            else:
                leaf.right = newNode
            newNode.parent = leaf
        else:
            self.root = newNode
        self.incrementParentsSize(newNode)
    
    def removeNodeFromParent(self, node, substitute=None, decrement=True):
        parent = node.parent
        if parent.left == node:
            parent.left = substitute
        else:
            parent.right = substitute
        if decrement:
            self.decrementParentsSize(node)
    
    def deleteNode(self, value):
        if self.root.value == value:
            node = self.root
            if not node.left and not node.right:
                self.root = None
            elif node.left and not node.right:
                self.root = node.left
                node.left = None
            elif node.right and not node.left:
                self.root = node.right
                node.right = None
            else:
                leaf = self.findLeaf(self.root)
                if leaf.left:
                    leaf = leaf.left
                elif leaf.right:
                    leaf = leaf.right
                self.removeNodeFromParent(leaf)
                self.root = leaf
                leaf.left = node.left
                leaf.right = node.right
                leaf.size = node.size
                if leaf.left:
                    leaf.left.parent = leaf
                if leaf.right:
                    leaf.right.parent = leaf
                node.left = None
                node.right = None
            self.root.parent = None
        else:
            node = self.findNode(value)
            if not node.left and not node.right:
                self.removeNodeFromParent(node)
            elif node.left and not node.right:
                self.removeNodeFromParent(node, node.left)
                node.left.parent = node.parent
                node.left = None
            elif node.right and not node.left:
                self.removeNodeFromParent(node, node.right)
                node.right.parent = node.parent
                node.right = None
            else:
                leaf = self.findLeaf(node)
                if leaf.left:
                    leaf = leaf.left
                    self.removeNodeFromParent(leaf)
                elif leaf.right:
                    leaf = leaf.right
                    self.removeNodeFromParent(leaf)
                else:
                    self.removeNodeFromParent(leaf)
                self.removeNodeFromParent(node, leaf, False)
                leaf.left = node.left
                leaf.right = node.right
                leaf.size = node.size
                leaf.parent = node.parent
                if leaf.left:
                    leaf.left.parent = leaf
                if leaf.right:
                    leaf.right.parent = leaf
                node.left = None
                node.right = None
            node.parent = None
        return node
    
    def printTree(self):
        if self.root:
            currentDepth = [self.root]
            newDepth = []
            while len(currentDepth) > 0:
                node = currentDepth.pop(0)
                if node.left:
                    newDepth.append(node.left)
                if node.right:
                    newDepth.append(node.right)
                if len(currentDepth) > 0:
                    print(node.value, end=' ')
                else:
                    currentDepth = newDepth
                    newDepth = []
                    print(node.value)

    def randomNode(self):
        current = self.root
        while current:
            options = ['self', 'left', 'right']
            weights = [1, current.leftSize, current.rightSize]
            outcome = random.choices(options, weights)[0]
            if outcome == 'self':
                return current
            elif outcome == 'left':
                current = current.left
            else:
                current = current.right