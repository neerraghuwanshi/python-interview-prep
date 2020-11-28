from stack import Stack


def QuickSortIterative(A):
    if len(A) < 2:
        return A

    B = Stack()
    B.push(0)
    B.push(len(A)-1)

    while len(B) > 0:
        high = B.pull()
        low = B.pull()
        p = partition(A, low, high)
        if high > p+1:
            B.push(p+1)
            B.push(high)
        if low < p-1:
            B.push(low)
            B.push(p-1)
    return A


def QuickSortRecursive(A):
    low = 0
    high = len(A) - 1
    return _QuickSortRecursive(A, low, high)

 
def partition(A, low, high):
    while low != high:
        if A[low] >= A[high]:
            A[low], A[high-1] = A[high-1], A[low]
            A[high], A[high-1] = A[high-1], A[high] 
            high -= 1
        else:
            low +=1
    return high


def _QuickSortRecursive(A, low, high):
    if low < high:
        part = partition(A, low, high)
        _QuickSortRecursive(A, low, part-1)
        _QuickSortRecursive(A, part+1, high)
    return A


A = [23, 25, 24, 22, 19, 20, 20]
print(QuickSortIterative(A))
A = [23, 25, 24, 22, 19, 20, 20]
print(QuickSortRecursive(A))