from collections import defaultdict

dictionar=defaultdict(set)
litere=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#print(litere[3])
for i in range (len(litere)):
    dictionar[litere[i]]="unknown"
#print(dictionar)
#     0123456789
hint="-d+w~h+g-t"
hint_word=list(hint)
print(hint_word)
hint_word=list(hint)
for i in range (10):
    if i%2==0:
        if dictionar[hint_word[i+1]] == "unknown" or dictionar[hint_word[i+1]=="yellow" and dictionar[hint_word[i]]=="+"]:
            dictionar.pop(hint_word[i+1])
            #dictionar[hint_word[i+1]]={}#SET
        if hint_word[i]=="+":
            dictionar[hint_word[i+1]].add("green")
            dictionar[hint_word[i+1]].add( ((i+1)//2)+1)
            #corp.add("green", ((i+1)//2)+1)
            #dictionar[hint_word[i+1]].values().add(((i+1)//2)+1)
        elif hint_word[i]=="-":
            dictionar[hint_word[i+1]].add("grey")
            dictionar[hint_word[i+1]].add(((i+1)//2)+1)
            #corp.add("grey",((i+1)//2)+1)
            #dictionar[hint_word[i+1]].values().add(((i+1)//2)+1) 
        elif hint_word[i]=="~":
            dictionar[hint_word[i+1]].add("yellow")
            dictionar[hint_word[i+1]].add(((i+1)//2)+1)
            #corp.add("yellow",((i+1)//2)+1)
            #dictionar[hint_word[i+1]].values().add(((i-1)//2)+1) 
    else: continue
print (dictionar)