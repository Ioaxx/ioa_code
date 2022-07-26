'''
with open("reduceri.txt") as data_file:
    for line in data_file:
        cuv = line.split()
        print(cuv)
        #if(cuv)
'''

        
from matplotlib.cbook import index_of


with open("madlib\\reduceri.txt") as f:
    lines = f.readlines()
    #print (lines)
    for line in lines:
        cuv = line.split()
        print (cuv)
        contor=0
        for litera in cuv:
            first_char = ""
            for i in range(0, 1):
                first_char = first_char + litera[i]
            #print("First character:", first_char)
            '''
            
            '''
            #if first_char is "<":
            if litera.startswith("<"):
                #print("write a:", lines[first_ct:last_ct])
                print("write a", litera[0:litera.find(">")+1])
                input()
        
        
        #............
        
      
    
        
        
        