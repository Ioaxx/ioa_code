'''
with open("reduceri.txt") as data_file:
    for line in data_file:
        cuv = line.split()
        print(cuv)
        #if(cuv)
'''

        
#from matplotlib.cbook import index_of


f= open("madlib\\reduceri.txt") 
lines = f.readlines()
#print (lines)
for line in lines:
    cuv = line.split()
    print (cuv)
    contor=0
    for litera in cuv:
        #print("First character:", first_char)
        #if first_char is "<":
        if litera.startswith("<"):
            #print("write a:", lines[first_ct:last_ct])
            print("write a", litera[0:litera.find(">")+1])
            input()
            
        
        #............
        
      
    
        
        
        