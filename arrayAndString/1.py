# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures


def unique(string):
    # if the characters are ASCII(128) or UNICODE(256)
    if len(string) > 128:
        return False
    array = []
    for char in string:
        if char in array:
            return False
        else:
            array.append(char)
    return True


str = 'Neer'

print(unique(str))