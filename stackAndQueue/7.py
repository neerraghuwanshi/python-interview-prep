"""
Make a list of balanced parenthesis on an integer input

Input: 3
Output:
    ((()))
    ()(())
    (())()
    (()())
    ()()()
"""


def parenthesisSetPermutation(n):
    parenthesisSetList = []
    if n > 0 and n < 9:
        unifiedParenthesisSet = ''
        for _ in range(n):
            unifiedParenthesisSet += '('
        for _ in range(n):
            unifiedParenthesisSet += ')'

        parenthesisSetList.append(unifiedParenthesisSet)
            
        for leftLayer in range(n-1):
            for rightLayer in range(n-1):
                newUnifiedParenthesisSet = unifiedParenthesisSet[:]
                first = newUnifiedParenthesisSet[:leftLayer+1]
                second = newUnifiedParenthesisSet[-rightLayer-2]
                third = newUnifiedParenthesisSet[leftLayer+2:-rightLayer-2]
                fourth = newUnifiedParenthesisSet[leftLayer+1]
                fifth = newUnifiedParenthesisSet[-rightLayer-1:]
                newUnifiedParenthesisSet = f'{first}{second}{third}{fourth}{fifth}'
                parenthesisSetList.append(newUnifiedParenthesisSet)
    return parenthesisSetList


def testParenthesisSet(parenthesisSet):
    openingParenthesisCount = 0
    for item in parenthesisSet:
        if item == '(':
            openingParenthesisCount += 1
        else:
            if openingParenthesisCount == 0:
                return False
            openingParenthesisCount -= 1
    if openingParenthesisCount == 0:
        return True
    return False


def testParenthesisSetPermutationList(parenthesisSetList):
    for parenthesisSet in parenthesisSetList:
        if not testParenthesisSet(parenthesisSet):
            return False
    return True
        

if __name__ == "__main__":
    
    for i in range(-2, 11):
        parenthesisSetList = parenthesisSetPermutation(i)
        print(parenthesisSetList)
        test = testParenthesisSetPermutationList(parenthesisSetList)
        if test == False:
            print(False)
            break
    else:
        print(True)