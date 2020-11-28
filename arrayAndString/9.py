# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").


def isSubstring(s1, s2):
    if s2 in s1:
        return True
    return False


def isRotation(s1, s2):
    for i in range(len(s2)):
        if s1 == s2[i:]+s2[:i]:
            return True
    return False


print(isRotation('waterbottle', 'erbottlewat'))