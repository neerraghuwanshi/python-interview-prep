# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


def rotateImage(lst):
    length = len(lst)
    new_lst = [[] for i in range(length)]
    
    for i in range(length):
        for j in range(length):
            new_lst[length-j-1].append(lst[i][j])

    return new_lst
    
    
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(rotateImage(lst))