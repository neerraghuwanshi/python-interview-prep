# Paths with Sum: You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).


def PathsWithSum(node, sum):
    if node:
        left = PathsWithSum(node.left, sum-node.value)
        right = PathsWithSum(node.right, sum-node.value)
        if node.value == sum:
            return left + right + 1
        return left + right
    return 0

def Paths(node, sum):
    if node:
        paths = PathsWithSum(node, sum)
        left = Paths(node.left, sum)
        rigth = Paths(node.right, sum)
        return left + rigth + paths
    return 0


# Optimized

def PathsOptimized(node, tagretSum, running=0, hashMap={}):
    if node:
        running += node.value
        total = hashMap.get(running-tagretSum, 0)
        if running == tagretSum:
            total += 1
        increment(hashMap, running, 1)
        left = PathsOptimized(node.left, tagretSum, running, hashMap)
        right = PathsOptimized(node.right, tagretSum, running, hashMap)
        total += left + right
        increment(hashMap, running, -1)
        return total
    return 0


def increment(hashMap, key, value):
    hashMap.setdefault(key, 0)
    hashMap[key] += value
    if hashMap[key] == 0:
        hashMap.pop(key)