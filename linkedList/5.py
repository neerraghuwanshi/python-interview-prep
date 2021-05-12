# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input:(7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295. 
# Output:2 -> 1 -> 9. Thatis,912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem. 
# EXAMPLE
# Input:(6 -> 1 -> 7) + (2 -> 9 -> 5). That is,617 + 295. 
# Output:9 -> 1 -> 2.Thatis,912.
from linkedList import LinkedList

    
def StringifyList(ll):
    string = ''
    node = ll.head
    while node:
        string += node.value
        node = node.next
    return string

def BackwordSum(ll1, ll2):
    s1 = StringifyList(ll1)
    s2 = StringifyList(ll2)
    s3 = str(int(s1[::-1]) + int(s2[::-1]))
    ll3 = LinkedList()
    for i in s3[::-1]:
        ll3.appendNode(i)
        
def ForwordSum(ll1, ll2):
    s1 = StringifyList(ll1)
    s2 = StringifyList(ll2)
    s3 = str(int(s1) + int(s2))
    ll3 = LinkedList()
    for i in s3:
        ll3.appendNode(i)
        
        
        
        
# With Recursion :)      
  
def sumLists(ll1, ll2):
    ll3 = LinkedList()
    node1 = ll1.head
    node2 = ll2.head
    
    while node1 or node2:
        if node1 and node2:
            node1 = node1.next
            node2 = node2.next
        elif node1:
            node1 = node1.next
            ll2.addAsHead(0)
        elif node2:
            node2 = node2.next
            ll1.addAsHead(0)
    
    node1 = ll1.head
    node2 = ll2.head
    
    def sumNodes(node1, node2):
        if node1 and node2:
            print('node1', node1.value)
            print('node2', node2.value)
            addition = node1.value + node2.value + sumNodes(node1.next, node2.next)
            print('addition', addition)
            if addition > 9:
                ll3.addAsHead(addition-10)
                return 1
            else:
                ll3.addAsHead(addition)
                return 0
        return 0
    
    carry = sumNodes(node1, node2)
    if carry == 1:
        ll3.addAsHead(1)

    return ll3
    