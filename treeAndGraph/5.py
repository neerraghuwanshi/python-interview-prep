# Validate BST: Implement a function to check if a binary tree is a binary search tree.


def validateBST(node, min=None, max=None):
    if not node:
        return True
    if (min and min > node.value) or (max and max <= node.value):
        return False
    return validateBST(node.left, min, node.value) and validateBST(node.right, node.value, max)