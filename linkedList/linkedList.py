class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def addAsHead(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current_head = self.head
            self.head = new_node
            new_node.next = current_head
            

    def appendNode(self, value):
        new_node = Node(value)
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
            return oldHead
        else:
            node = self.head
            for _ in range(index-1):
                node = node.next
            nextNode = node.next
            node.next = nextNode.next
            nextNode.next = None
            return nextNode
                
            
    def appendAfterValue(self, value, nodeValue):
        newNode = Node(value)
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