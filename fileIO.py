#Extracting a line from the file
""" with open("fileio.txt",'r') as f:
    lines=0
    for line in f:
        line=line.rstrip()
        # print(line)
        #Couting the lines-
        lines+=1
        if line.startswith("Email:"):
            print(line)
        if not 'Apurbo' in line:
            continue
        print(line)
print(lines)   """
#Extracting a word from the file

with open('fileio.txt','r') as f:
    data=f.readlines() #Store all the datas in a list
    for line in data:
        if 'Monaghan' in line:
            splitted=line.split()
            print(splitted)
            for word in splitted:
                if 'Monaghan' in word:
                    print('Monaghan')