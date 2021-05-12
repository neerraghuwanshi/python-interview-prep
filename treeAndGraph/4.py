# Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.


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
            print(node.value)
            self.printTree(node.left)
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
                
                
tree = Tree()
tree.root = Node2(1)
tree.root.left = Node2(2)
tree.root.right = Node2(3)
tree.root.left.left = Node2(4)
tree.root.left.right = Node2(5)
tree.root.left.left.left = Node2(6)
# tree.root.left.left.left.left = Node2(7)



def checkBalanced(node):
    if not node:
        return 1
    
    leftHeight = isBalanced(node.left)
    if leftHeight == -1:
        return -1
    
    rightHeight = isBalanced(node.right)
    if rightHeight == -1:
        return -1
    
    if abs(leftHeight - rightHeight) > 1:
        return -1
    
    return max(leftHeight, rightHeight) + 1



def isBalanced(node):
    num = checkBalanced(node)
    return num

print('----')
print(isBalanced(tree.root))