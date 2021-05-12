# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
# EXAMPLE
# lnput:the node c from the linked lista->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks likea->b->d->e- >f
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


def deleteNode(ll, value):
        if ll.head.value == value:
            oldHead = ll.head
            ll.head = ll.head.next
            oldHead.next = None
        else:
            node = ll.head
            while node and node.next:
                if node.next.value == value:
                    nextNode = node.next
                    node.next = nextNode.next
                    nextNode.next = None
                    break
                node = node.next