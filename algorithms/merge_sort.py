def MergeSortIterative(A):
    length = len(A)
    B = MakeList(A, length)
    C = reduce(B)
    return C


def MergeSortRecursive(A):
    if len(A) <= 1:
        return A
    mid = len(A)//2
    left = MergeSortRecursive(A[:mid])
    right = MergeSortRecursive(A[mid:])
    print(left, right)
    C = merge(left, right)
    return C


def merge(A, B):
    C = []
    while (len(A) > 0) and (len(B) > 0):
        if A[0] < B[0]:
            C.append(A[0])
            A.pop(0)
        else:
            C.append(B[0])
            B.pop(0)
    C += A + B
    return C


def MakeList(A, length):
    B = []
    n = 0
    while n+1 < length: 
        if A[n] > A[n+1]:
            B.append([A[n+1], A[n]])
        else:
            B.append([A[n], A[n+1]])
        n += 2
    if n != length:
        C = merge(B.pop(), [A[-1]])
        B.append(C)
    return B


def compare(A):
    B = []
    j = 0
    while j+1 < len(A):
        C = merge(A[j], A[j+1])
        B.append(C)
        j += 2
    if j < len(A):
        B.append(A[-1])
    return B


def reduce(B):
    while len(B) != 1:
        C = compare(B)
        B = C
    return B[-1]


A = [8, 7, 6, 5, 4, 3, 2, 10]
print(MergeSortIterative(A))
A = [8, 7, 6, 5, 4, 3, 2, 10]
print(MergeSortRecursive(A))