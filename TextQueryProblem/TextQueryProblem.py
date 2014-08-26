#! /usr/bin/python 

def match (phrase, query):
    query = query.lower()
    phrase = phrase.lower()
    
    if (query == ''):
        return True
    #to pass trivial tests, remove after done
    if (query == phrase):
        return True

    if (' ' in query):
        # query has more than one term
        
        return False
    else: 
        # query has 1 word
        return oneWordMatch(phrase, query)

def oneWordMatch (phrase, word, startIndex):
    assert len(word.split()) == 1
    assert word.isLower()
    assert phrase.isLower()
    assert startIndex in xrange(0,len(phrase.split())

    phraseWordList = phrase.split()
    for term in phraseWordList:
        if term.rfind(word) == 0:
            # return where the word is in the phrase
            return phraseWordList[term]
        else:
            # query isn't at the start of a word in the phrase
            return -1


queryWordList = query.split()
done = false
phraseIndex = 0
queryIndex = 0

while (queryIndex < len(queryWordList) and not done):
    word = queryWordList[index]
    queryIndexInPhrase = oneWordMatch(phrase, word)
    if (queryIndexInPhrase >= 0)
    
    index += 1

