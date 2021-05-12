# Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.


def in_order_successor(inputNode):
    if inputNode is None:
        return None

    if inputNode.right:
        current = inputNode.right
        while current.left:
            current = current.left
        return current

    ancestor = inputNode.parent
    child = inputNode
    while ancestor and ancestor.right == child:
        child = ancestor
        ancestor = ancestor.parent
    return ancestor