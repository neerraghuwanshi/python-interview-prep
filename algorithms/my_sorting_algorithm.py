def MySortingAlgorithm(A):
    first = 0
    second = 1
    while second != len(A):
        first_value = A[first]
        second_value = A[second]
        if first_value > second_value:
            A[first] = second_value
            A[second] = first_value
        first += 2
        second += 2
    return A


A = [21, 4, 1, 3, 9, 20, 25, 6]
