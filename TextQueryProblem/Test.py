#!/usr/bin/env python

import TextQueryProblem as t
import sys

def testTrivial():
    check ('dog','candy', t.match, False)
    check ('dog', 'dog', t.match, True)
    check ('Hello world', 'Hello world', t.match, True)
    check ('doG', 'dog', t.match, True)
    check ('HelLo WoRLD', 'Hello world', t.match, True)
    check ('cat', 'location', t.match, False)
    
def testWithSpaces():
    check ('cats hats', 'the cats hats', t.match, True)
    check ('catshats', 'the cats hats', t.match, True)
    check ('luke bryant john', 'Luke Bryant Johnston', t.match, True)
    check ('luke bry john', 'Luke Bryant Johnston', t.match, False)
    check ('lu ke', 'luke Bryant Johnston', t.match, True)
    
    return False

def testEdgeCases():
    check ('', '', t.match,True)



def check(query, phrase, function, result):
    if (function(phrase, query) == result):
        print "PASSED"
    else: 
        print "FAILED: " + query + " in " + phrase + " expecting " + str(result)

testTrivial()
testEdgeCases()
testWithSpaces()
