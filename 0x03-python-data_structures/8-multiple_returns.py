#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != 0:
        return(len(sentence), sentence[0])
    else:
        sentence[0] = None
        return(len(sentence), sentence[0])
