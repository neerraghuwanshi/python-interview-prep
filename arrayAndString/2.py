# Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutation(string1, string2):
    
    if len(string1) != len(string2):
        return False
    
    dict = {}
    for i in string1:
        if i in dict:
            dict[i].append(0)
        else:
            dict[i] = [0]
            
    for i in string2:
        if i in dict and len(dict[i]) > 0:
            dict[i].pop()
        else:
            return False
    return True


print(checkPermutation('neer', 'neer'))