###
# Class owning the set of hints given in the course
# of playing one game of Wordle
class WordChecker:

    dictionar={}
    litere=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #print(litere[3])
    for i in range (len(litere)):
        dictionar[litere[i]]="unknown"
    #print(dictionar)
    ###
    
    # Class constructor:
    def __init__(self):
        print(f"TODO: WordChecker is initialized")
        self.hint_word = ""

    ###
    # Updates the internal state of the checker with a new hint
    def update(self, hint, hint_word=None):
        print(f"TODO: WordChecker adding the hint: '{hint}'.")
        '''
        dictionar pe litere, adaugam culoarer si pozitii,
        primim ca parametru "hint " cu tilda plusuri si minusuri si tilda
        '''
        
        self.hint_word=list(self.hint)
        for i in range (10):
            if i%2==0:                                          #if we reset
                if dictionar[self.hint_word[i+1]] == "unknown" #or dictionar[self.hint_word[i+1]=="yellow" and dictionar[hint_word[i]]=="+"]:
                    dictionar.pop(self.hint_word[i+1])
                    #dictionar[hint_word[i+1]]={}#SET
                if self.hint_word[i]=="+":
                    dictionar[self.hint_word[i+1]].add("green")
                    dictionar[self.hint_word[i+1]].add( ((i+1)//2)+1)
                    #corp.add("green", ((i+1)//2)+1)
                    #dictionar[hint_word[i+1]].values().add(((i+1)//2)+1)
                elif self.hint_word[i]=="-":
                    dictionar[self.hint_word[i+1]].add("grey")
                    dictionar[self.hint_word[i+1]].add(((i+1)//2)+1)
                    #corp.add("grey",((i+1)//2)+1)
                    #dictionar[hint_word[i+1]].values().add(((i+1)//2)+1) 
                elif self.hint_word[i]=="~":
                    dictionar[self.hint_word[i+1]].add("yellow")
                    dictionar[self.hint_word[i+1]].add(((i+1)//2)+1)
                    #corp.add("yellow",((i+1)//2)+1)
                    #dictionar[hint_word[i+1]].values().add(((i-1)//2)+1) 
            else: continue
        
    
    
    
    
     ###
     # Checks whether a given word matches all known hints
    def check(self, word):
        print(f"TODO: WordChecker testing if '{word}' verifies all known hints.")
        return True
        
    ###
    # Returns a string representation of the entire object
    def __str__(self):
        return f"TODO: WordChecker internal state."

###
# WordChecker test code
if __name__ == "__main__":
    # creates a test WordChecker object and run through its methods
    wordChecker = WordChecker()
    wordChecker.update("some hint")
    print(wordChecker.check("some word"))
    print(wordChecker)