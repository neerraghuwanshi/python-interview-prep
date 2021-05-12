# Implement a function to check if a linked list is a palindrome.


from stackAndQueue.stack import Stack


def checkPalindrome(ll):
    A = []
    node = ll.head
    while node:
        A.append(node.value)
        node = node.next
    for i in range(len(A)//2):
        if A[i] != A[-i]:
            return False
    return True


# 0 space N time solution

def reverse(node):
    prev = None
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next
    return prev


def isPalindrome(ll):
    node1 = ll.head
    node2 = ll.head
    prev = None
    
    while node2 and node2.next:
        prev = node1
        node1 = node1.next
        node2 = node2.next.next
        
    if not node2:
        prev.next = None
        return isEqual(ll.head, node1)
    elif not node2.next:
        prev = node1
        node1 = node1.next
        prev.next = None
        return isEqual(ll.head, node1)
    

def isEqual(node1, node2):
    node2 = reverse(node2)
    while node2:
        if not node2.value == node1.value:
            return False
        node2 = node2.next
        node1 = node1.next
    return True
        

print(isPalindrome(ll))