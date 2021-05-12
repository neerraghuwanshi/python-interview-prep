# Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [thesameCasearlier]
# Output: C


def LoopDetection(ll):
    dict = {}
    node = ll.head
    while node:
        if node.value in dict:
            return True
        else:
            dict[node.value] = 0
            node = node.next
    return False


def isLoop(ll):
    node1 = node2 = ll.head
    while node2 and node2.next:
        node1 = node1.next
        node2 = node2.next.next
        if node2 == node1:
            node1 = ll.head
            while node1 != node2:
                node1 = node1.next
                node2 = node2.next
            return node1.value
    return False