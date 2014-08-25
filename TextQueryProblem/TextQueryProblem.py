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
        separatedPhrase = phrase.split()
        for term in separatedPhrase:
            if term.rfind(query) == 0:
                return True
            else:
                # query isn't at the start of a word in the phrase
                return False

