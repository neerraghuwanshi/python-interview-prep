# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true 
# pales, pale -> true 
# pale, bale -> true 
# pale, bake -> false


def checkEdits(string1, string2):
    j = 0
    
    if len(string1) < len(string2):
        for i in range(len(string2)):
            if string1[i-j:i-j+1] != string2[i]:
                j += 1
    elif len(string1) > len(string2):
        for i in range(len(string1)):
            if string2[i-j:i-j+1] != string1[i]:
                j += 1
    else:
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                j += 1
    
    if j <= 1:
        return True
    return False

print(checkEdits('neer', 'neen'))