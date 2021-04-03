# -*- coding: utf-8 -*-
"""
Spyder Editor

ANAGRAMs
"""


strs = ["bottom","tombot","test","estt","tets","ankit","tikna","love","arnav","vanra"]
h_map = {}

for word in strs :
    key =  str(sorted(word))
    #print(strsSorted)
    #strsSortedList += strsSorted
    if key not in h_map:
        h_map[key]=[]
    h_map[key].append(word)
 
    
#print(h_map.keys())   
print(h_map.values())    
    
     