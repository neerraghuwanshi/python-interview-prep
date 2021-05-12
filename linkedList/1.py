# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?


from linkedList import LinkedList


ll = LinkedList()
ll.appendNode(1)
ll.appendNode(2)
ll.appendNode(2)
ll.appendNode(1)
ll.appendNode(2)
ll.appendNode(3)
ll.appendNode(3)
ll.appendNode(4)
ll.appendNode(4)
ll.appendNode(5)
ll.appendNode(5)
# ll.printList()
print('-----------')


def removeDups(ll):
    node = ll.head
    while node:
        checkNode = node.next
        prevCheckNode = node
        while checkNode:
        print(node.value)
            if node.value == checkNode.value:
                prevCheckNode.next = checkNode.next
                checkNode.next = None
                checkNode = prevCheckNode.next
            else:
                prevCheckNode = checkNode
                checkNode = checkNode.next
        node = node.next            
                
removeDups(ll)    
# ll.printList()