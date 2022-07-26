with open("test.txt",'r') as data_file:
    for cuvant in data_file:
        data = cuvant.split()
        print(data)