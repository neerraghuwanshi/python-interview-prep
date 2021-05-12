# Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create analgorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.


def checkValues(node1, node2):
    if not node1 and not node2:
        return True
    elif node1 and node2:
        if node1.value == node2.value:
            return checkValues(node1.left, node2.left) and checkValues(node1.right, node2.right)
        else:
            return checkValues(node1.left, node2) or checkValues(node1.right, node2)
    return False


def checkSubtree(t1, t2):
    node1 = t1.root
    node2 = t2.root
    return checkValues(node1, node2)