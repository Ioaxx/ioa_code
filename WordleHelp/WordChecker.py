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
        
        hint_word=list(hint)
        for i in range (10):
            if i%2==0:
                if dictionar[hint_word[i+1]] == "unknown":
                    dictionar.pop(hint_word[i+1])
                if hint_word[i]=="+":
                    dictionar[litere[i+1]]="green"
                    dictionar[litere[i+1]]= (i+1)//2
                elif hint_word[i]=="-":
                    dictionar[litere[i+1]]="grey"
                    dictionar[litere[i+1]]= (i+1)//2
                elif hint_word[i]=="~":
                    dictionar[litere[i+1]]="yellow"
                    dictionar[litere[i+1]]= (i+1)//2
        
    
    
    
    
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