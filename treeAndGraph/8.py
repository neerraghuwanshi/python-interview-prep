# First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.


# With link to parent

def findArrayParent(node):
    current = node
    array = []
    while current:
        array.append(current)
        current = current.parent
    return array[::-1]

def FCAParent(node1, node2):
    array1 = findArrayParent(node1)
    array2 = findArrayParent(node2)
    
    i = 0
    while array1[i] and array2[i]:
        if array1[i+1].value != array2[i+1].value:
            return array1[i]
        i += 1
        
        

# With no link to parent

def findPath(node, findNode):
    if node:
        if node == findNode:
            return [node]
        l = findPath(node.left, findNode)
        if l:
            l.append(node)
            return l
        r = findPath(node.right, findNode)
        if r:
            r.append(node)
            return r
    return False
    

def firstCommomAncestor(tree, node1, node2):
    A = findPath(tree.root, node1)[::-1]
    B = findPath(tree.root, node2)[::-1]
    
    if len(A) < len(B):
        smallerList = A
    else:
        smallerList = B
        
    for index in range(len(smallerList)):
        if A[index] != B[index]:
            return smallerList[index-1]
    
    if len(smallerList) > 1:
        return smallerList[-2]
    return smallerList[-1]