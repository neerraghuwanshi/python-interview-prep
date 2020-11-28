def BubbleSortIterative(A):
    length = len(A)
    for i in reversed(range(1, length)):
        j = 0
        while j != i:
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            j += 1
    return A


def BubbleSortRecursive(A):
    length = len(A)
    return _BubbleSortRecursive(A, length)


def _BubbleSortRecursive(A, length):
    if length < 2:
        return A 
    i = 0
    while i+1 < length:
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
        i += 1
    return _BubbleSortRecursive(A, length-1)


A = [12, 13, 14, 10, 8, 11, 0, 1]
print(BubbleSortIterative(A))
print(BubbleSortRecursive(A))