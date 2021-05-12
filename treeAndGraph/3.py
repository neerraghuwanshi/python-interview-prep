# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).


# from linkedList.linkedList import LinkedList


        
class Node1:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
            
    def __init__(self, head=None):
        self.head = head

    def appendNode(self, value):
        new_node = Node1(value)
        if self.head == None:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
            
    def deleteNodeAtIndex(self, index):
        if index == 0:
            oldHead = self.head
            self.head = self.head.next
            oldHead.next = None
        else:
            node = self.head
            for i in range(index-1):
                node = node.next
            nextNode = node.next
            node.next = nextNode.next
            nextNode.next = None
                
            
    def appendAfterValue(self, value, nodeValue):
        newNode = Node1(value)
        node = self.head
        while node:
            if node.value == value:
                newNode.next = node.next
                node.next = newNode
            node = node.next
            
    def printList(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next
            
            
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

tree.appendChild(1)
tree.appendChild(2)
tree.appendChild(3)
tree.appendChild(4)
tree.appendChild(5)
tree.appendChild(6)
# tree.printTree(tree.root)


def listOfDepths(treeNode):
    depthList = []
    currentDepth = LinkedList()
    currentDepth.appendNode(treeNode)
    
    while currentDepth.head:
        newDepth = LinkedList()
        llNode = currentDepth.head
        while llNode:
            if llNode.value.left:
                newDepth.appendNode(llNode.value.left)
            if llNode.value.right:
                newDepth.appendNode(llNode.value.right)
            llNode = llNode.next
        depthList.append(currentDepth)
        currentDepth = newDepth
        
    return depthList


def listOfDepths2(root):
    A = [LinkedList()]
    A[0].appendNode(root)
    i = 0
    while A[i].head:
        A.append(LinkedList())
        node = A[i].head
        while node:
            if node.value.left:
                A[i+1].appendNode(node.value.left)
            if node.value.right:
                A[i+1].appendNode(node.value.right)
            node = node.next
            print('next', node)
        i += 1
    return A[:-1]


ll = listOfDepths2(tree.root)


for item in ll:
    print('--')
    node = item.head
    while node:
        print(node.value.value)
        node = node.next
        

# Most Optimal
def listOfDepths3(treeNode):
    depthList = []
    currentDepth = LinkedList()
    currentDepth.appendNode(treeNode)
    
    while currentDepth.head:
        newDepth = LinkedList()
        llNode = currentDepth.head
        while llNode:
            if llNode.value.left:
                newDepth.appendNode(llNode.value.left)
            if llNode.value.right:
                newDepth.appendNode(llNode.value.right)
            llNode = llNode.next
        depthList.append(currentDepth)
        currentDepth = newDepth
        
    return depthList