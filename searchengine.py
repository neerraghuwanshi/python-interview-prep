lst= ["i love you", "i love the way you do it", "python is python", "python is great"]
search = input("search for what you like\n")

def matching_words(sentence1,sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score

scores = [matching_words(search,sentence)for sentence in lst]
sortingSentScores = [sentscore for sentscore in sorted(zip(scores,lst),reverse = True) if sentscore[0] !=0]

print(f"{len(sortingSentScores)} Results found:")
for first,second in sortingSentScores:
    print(second)

