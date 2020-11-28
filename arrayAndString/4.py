# Given a string, write a function to check if it is a permutation of a palin­drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)


def checkPalindromePermutation(string):
    odd = 0
    dict = {}
    
    for i in string:
        if i in dict:
            dict[i].append(0)
        else:
            dict[i] = [0]
        if len(dict[i]) % 2 == 1:
            odd += 1
        else:
            odd -= 1
    
    if i <= 1:
        return True
    return False