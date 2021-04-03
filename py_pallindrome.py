# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 08:45:52 2020
pallindrom.py
@author: ankit
"""



strs = ["dum","mud","tom","arnav","vanra"]
concatOp = []


for word in strs:
    #wordRev = str.reversed(word) - below code to reverse the words
    wordRev = ''
    index = len(word)
 #   print(index)
    while index >= 1 :
 #       print(word[index-1]) 
        wordRev = wordRev+word[index-1] 
        index = index -1
    
#    print(wordRev)
    if wordRev in strs:
        concatOp.append(word+wordRev)
        
print(concatOp)       