# Implement an algorithm to find the kth to last element of a singly linked list.


from linkedList import LinkedList


ll = LinkedList()
ll.appendNode(1)
ll.appendNode(2)
ll.appendNode(2)
ll.appendNode(1)
ll.appendNode(2)
ll.appendNode(3)
ll.appendNode(4)
ll.appendNode(4)
ll.appendNode(5)
ll.appendNode(5)


def FindElementFromLast(ll, index):
    node = ll.head
    A = []
    while node:
        A.append(node.value)
        node = node.next
    print(A[-index])
    

FindElementFromLast(ll, 5)