# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.


def setZero(lst):
    length = len(lst)
    zeroList = [0 for i in range(length)]
    zeroCoordinatesList = []
    
    for i in range(length):
        for j in range(length):
            if lst[i][j] == 0:
                zeroCoordinatesList.append((i, j))
    
    
    for zeroCoordinates in zeroCoordinatesList:
        lst[zeroCoordinates[0]] = zeroList
        for i in range(length):
            lst[i][zeroCoordinates[1]] = 0

    return lst
    
    
lst = [
    [0, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]

print(setZero(lst))