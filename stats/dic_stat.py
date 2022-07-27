f= open("stats\\words.txt")
dictionar = {}
lines = f.readlines()
for line in lines:
    cuv = line.split()
    for i in range(1) :
        dictionar[cuv[0]]=cuv[1]
#print(dictionar)

litere=["abcdefghijklmnopqrstuvwxyz"]
sorted(dictionar.values())
print(dictionar)
def starts_in ():
    #for i in range(len(litere))
    #for cuv in dictionar
     contor=0
     for cuv in dictionar.keys:
        contor_litere=0
        if cuv[0] == litere[contor]:
            contor_litere+=1
        else :
            print(contor_litere, "incep cu ", litere[contor] )
            contor+=1
            contor_litere=0   
starts_in ()