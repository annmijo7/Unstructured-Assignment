import glob
import string
import sys
import os
from collections import defaultdict
listofdocs=[]
map=[]
count=0
line="1"
print("Enter document names and press the enter key. Enter 0 when done listing documents. ")
for line in sys.stdin:
        line=line.strip("\n")
        if (line=="0"):
            print("yes")
            break
        else:
            listofdocs.append(line)
    #f = open(str(line), 'r')
for docno in range(0,len(listofdocs)):
    #Importing file and reading
    f = open(listofdocs[docno], 'r')
    content=f.read()
    #Changing all words to lower case
    content=content.lower()
    
    #Splitting string and putting in list
    words=content.split()
    
    #Removing punctuation marks
    table = str.maketrans('', '', string.punctuation)
    words = [w.translate(table) for w in words]
    # Getting in the form word:[
    for i in range(0,len(words)):
        
        if (words[i] not in ["and","but","is","the","to"]):
            count=count+1
            l=[]
            l.append(words[i])
            map.append(l)
            l=[]
            l.append(docno+1)
            l.append(i+1)            
            (map[count-1]).append(l)

#Sorting
map.sort()
for item in map:
    print(item)

#Reducer

invind=defaultdict(list)
for item in range(0,len(map)-1):
    if (map[item][0] == map[item+1][0]):
        if (map[item][1] not in invind[map[item][0]]):
            invind[map[item][0]].append(map[item][1])
        if (map[item+1][1] not in invind[map[item][0]]):
            invind[map[item][0]].append(map[item+1][1])
print(invind)
