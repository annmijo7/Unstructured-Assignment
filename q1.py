import sys
import os
import string
#Q1------------------
#Puts text files in a list
import glob
from collections import defaultdict
docs=glob.glob('*.txt')
invind=defaultdict(list)
for docno in range(0,len(docs)):
    #Importing file and reading
    f = open(docs[docno], 'r')
    content=f.read()

    #Changing all words to lower case
    content=content.lower()
    
    #Splitting string and putting in list
    words=content.split()
    
    #Removing punctuation marks
    #table = str.maketrans('', '', string.punctuation)
    #words = [w.translate(table) for w in words]

    #for each word in document, add document number and position in inverted index
    for i in range(0,len(words)):
        if (words[i] not in ["and","but","is","the","to"]):
            invind[words[i]].append((docno+1,i+1))
#Inverted index with the word : (document number, position in document)            
#print("The inverted index is as follows: ")
print(invind)

#Q2---------------------
#Searching documents based on given query
def q_search(query):
    query=query.split()
    new_list=[]
    output=[]
    for word in range(0,len(query)):
        if(word%2==1):
            list_word1=[]
            list_word2=[]
            for n in invind[query[word-1]]:
                list_word1.append(n[0])
            for n in invind[query[word+1]]:
                list_word2.append(n[0])
            if (query[word]=="AND"):
                output=(set(list_word1) & set(list_word2))
            elif (query[word]=="OR"):
                output=(set(list_word1) | set(list_word2))
            else:
                print("Invalid boolean operator! ")
            
    if(len(output)==0):
        print("No documents")
    else:
        print(output)
        for id in output:
            print("Document ID: ",id,", Document Name: ",docs[id-1])
        
        
#Given a word, giving the documents it is present in and its positional indexes
def w_search(word):
    if (word in invind):
        print(word,"is in : ", invind[word])
    else:
        print("The word '", word, "' is not in the corpus.")

ui=1
while(ui!="0"):
    ui=input("Enter 1 for querying and 2 for searching for a specific word or 0 to exit: ")
    if (ui=="1"):
        query=input("Enter query: ")
        q_search(query)
    elif (ui=="2"):
        word=input("Enter word: ")
        w_search(word)




