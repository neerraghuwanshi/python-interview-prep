# Given two (singly) linked lists, determine if the two lists intersect. Return the inter­ secting node. Note that the intersection is defined based on reference, not value.That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.


from linkedList import LinkedList

ll1 = LinkedList()
ll1.appendNode(11)
ll1.appendNode(3)
ll1.appendNode(8)
ll1.appendNode(5)
ll1.appendNode(10)
ll1.appendNode(2)
ll1.appendNode(12)

ll2 = LinkedList()
ll2.appendNode(11)
ll2.appendNode(3)
ll2.appendNode(8)
ll2.appendNode(5)
ll2.appendNode(10)
ll2.appendNode(2)
ll2.appendNode(12)


def CheckIntersection(ll1, ll2):
    node1 = ll1.head 
    node2 = ll2.head 
    dict = {}
    while node1:
        dict[node1.value] = node1.next
        node1 = node1.next
    while node2:
        if node2.value in dict:
            if node2.next and dict[node2.value]:
                if node2.next.value == dict[node2.value].value:
                    print(node2.value)
                
            elif node2.next == dict[node2.value]:
                print(node2.value)
        node2 = node2.next
        
        
CheckIntersection(ll1, ll2)



# Efficient
def intersection(ll1, ll2):
    node1, node2 = compareLengths(ll1, ll2)
    
    while node1 and node2:
        if node1.value == node2.value:
            return True
        node1 = node1.next
        node2 = node2.next
    return False
        

def compareLengths(ll1, ll2):
    node1 = ll1.head
    node2 = ll2.head
    while node1 and node2:
        node1 = node1.next
        node2 = node2.next
    if node1:
        node2 = ll2.head
        while node1:
            node1 = node1.next
            node2 = node2.next
        return ll1.head, node2
    elif node2:
        node1 = ll1.head
        while node2:
            node1 = node1.next
            node2 = node2.next
    return ll1.head, ll2.head