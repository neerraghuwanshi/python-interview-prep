# BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting each element. Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
# EXAMPLE
# Input: Binary Tree
# Output: {2, 1, 3}, {2, 3, 1}


import random


class SNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        
    def push(self, value):
        node = SNode(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def popStart(self):
        oldHead = self.head
        if not oldHead.next: 
            self.head = None
            self.tail = None
        else:
            self.head = oldHead.next
        oldHead.next = None
        return oldHead
    
    def isEmpty(self):
        if not self.head:
            return True
        return False


class Node:
    def __init__(self, value):
        self.size = 1
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
                
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


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def findLeaf(self, node):
        s = Stack()
        s.push(node)
        while not s.isEmpty():
            node = s.popStart().value
            if node.left and node.right:
                s.push(node.left)
                s.push(node.right)
            else:
                return node
            
    def incrementParentSize(self, node):
        if node.parent:
            node.parent.size += 1
            self.incrementParentSize(node.parent)
            
    def decrementParentSize(self, node):
        if node.parent:
            node.parent.size -= 1
            self.incrementParentSize(node.parent)
                
            
    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
        else:
            node = self.findLeaf(self.root)
            newNode.parent = node
            incrementParentSize(newNode)
            if not node.left:
                node.left = newNode
            else:
                node.right = newNode
                
                
    def printTree(self, node):
        A = [node]
        while A:
            node = A.pop(0)
            print(node.value)
            if node.left:
                A.append(node.left)
            if node.right:
                A.append(node.right)
    
    
    def checkNode(self, node, value):
        if node.value == value:
            return True
        leftCheck = False
        rightCheck = False
        if node.left:
            leftCheck = self.checkNode(node.left, value)
        if node.right:
            rightCheck = self.checkNode(node.right, value)
        return leftCheck or rightCheck
    
    
    def find(self, value):
        return self.checkNode(self.root, value)
    
    
    def removeNodeFromParent(self, node, subsitute=None):
        parent = node.parent
        if parent.left and parent.left.value == node.value:
            parent.left = subsitute
        else:
            parent.right = subsitute
            
    
    def removeLeaf(self, node):
        if node:
            node.parent = None
            if node.left and node.right:
                return (self.removeLeaf(node.left) or
                self.removeLeaf(node.right))
            elif node.left:
                left = node.left
                self.decrementParentSize(left)
                node.left = None
                return left
            elif node.right:
                right = node.right
                self.decrementParentSize(right)
                node.right = None
                return right
            else:
                self.decrementParentSize(node)
                self.removeNodeFromParent(node)
                return node
    
    
    def deleteNode(self, node, value):
        if node:
            if node.value == value:
                leaf = self.removeLeaf(node)
                if not leaf.value == node.value:
                    leaf.size = node.size
                    leaf.left = node.left
                    leaf.right = node.right
                    leaf.parent = node.parent
                    self.removeNodeFromParent(node, leaf)
                    return node
                return leaf
            l = self.deleteNode(node.left, value)
            r = self.deleteNode(node.right, value)
            return l or r

    
    def delete(self, value):
        root = self.root
        if root.value == value:
            if root.left and root.right:
                leaf = self.removeLeaf(root)
                leaf.left = root.left
                leaf.right = root.right
                leaf.size = leaf.leftSize + leaf.rightSize
                leaf.parent = None
                self.root = leaf
            elif root.left:
                self.root = root.left
                root.left = None
                root.parent = None
            elif root.right:
                self.root = root.right
                root.right = None
                root.parent = None
            else:
                self.root = None
            return root
        else:
            l = self.deleteNode(root.left, value)
            r = self.deleteNode(root.right, value)
            return l or r
        
        
    def getRandomNode(self):
        current = self.root
        while current:
            choices = ['self', 'left', 'right']
            weights = [1, current.leftSize, current.rightSize]
            outcome = random.choices(choices, weights)[0]
            if outcome == "self":
                return current
            elif outcome == "left":
                current = current.left
            elif outcome == "right":
                current = current.right
        
        
bt = BinaryTree()
bt.insert(4)
bt.insert(2)
bt.insert(6)
bt.insert(1)
bt.insert(3)
# bt.insert(5)
# bt.insert(7)


# def BSTSequences(tree):
#     A = []
#     return A


def find_bst_sequences(bst):
    if not bst.root:
        return []
    return helper(bst.root)


def helper(node):
    if not node:
        return [[]]

    right_sequences = helper(node.right)
    left_sequences = helper(node.left)
    sequences = []
    for right in right_sequences:
        for left in left_sequences:
            sequences = weave(left, right, [node.value], sequences)
    return sequences


def weave(first, second, prefix, results):
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return results

    head = first[0]
    prefix.append(head)
    results = weave(first[1:], second, prefix, results)
    prefix.pop()
    head = second[0]
    prefix.append(head)
    results = weave(first, second[1:], prefix, results)
    prefix.pop()
    return results


print(find_bst_sequences(bt))