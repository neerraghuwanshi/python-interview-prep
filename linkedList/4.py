# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5] 
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
from linkedList import LinkedList

ll = LinkedList()
ll.appendNode(11)
ll.appendNode(3)
ll.appendNode(8)
ll.appendNode(5)
ll.appendNode(10)
ll.appendNode(2)
ll.appendNode(12)


def Partition(ll, value):
    node = ll.head.next
    prev = ll.head
    dict = {}
    while node:
        if node.value < value:
            prev.next = node.next
            old_head = ll.head
            ll.head = node
            node.next = old_head
            node = prev.next
        else:
            prev = node
            node = node.next
        
Partition(ll, 5)
ll.printList()