# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 06:53:00 2021

@author: ankit
"""


# Data File - file_email_py.txt
# C:\Users\ankit\test_data\file_email_py.txt
# show the email and count the highest num of times a email appeared after From: in each line
# DICTIONARY


handle = open(r"C:\Users\ankit\test_data\file_email_py.txt")
count = dict()

for line in handle:
    words = line.split()
    #print(words)
    
    if len(words) < 2 or words[0].startswith("From:") or not words[0].startswith("From"):
        continue
    email = words[1]
    count[email] = count.get(email,0) + 1
    #print(count)
    
    
highestword = None
highestcount = None
print(count.items())
for word, count in count.items():
    if highestcount is None or highestcount < count:
        highestcount = count
        highestword = word

print(highestword, highestcount)    
        