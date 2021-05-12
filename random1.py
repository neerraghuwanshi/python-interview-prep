def checkPalindrome(string):    
    i = 0
    j = len(string) - 1
    while i < j:
        print(string[i], string[j])
        if not string[i].isalnum():
            i += 1
            continue
        if not string[j].isalnum():
            j -= 1
            continue
        if string[i].lower() == string[j].lower():
            i += 1
            j -= 1
        else:
            return False
    return True