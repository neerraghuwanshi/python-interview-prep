def BinarySearchIterative(A, item):
    low = 0
    high = len(A) - 1
    mid = high//2 
    while low != high:
        if A[mid] > item:
            high = mid - 1
        elif A[mid] < item:
            low = mid + 1
        else:
            return True
        mid = (low + high) // 2
    return False


def BinarySearchRecusrsive(A, item):
    low = 0
    high = len(A) - 1
    return _BinarySearchRecusrsive(A, low, high, item)


def _BinarySearchRecusrsive(A, low, high, item):
    mid = (low + high) // 2 
    if low == high:
        return False
    if A[mid] > item:
        return _BinarySearchRecusrsive(A, low, mid-1, item)
    elif A[mid] < item:
        return _BinarySearchRecusrsive(A, mid+1, high, item)
    else:
        return True

A = [1, 3, 4, 5, 8, 11, 20, 30, 35]
print(BinarySearchIterative(A, 20))
print(BinarySearchRecusrsive(A, 20))