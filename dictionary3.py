#The general pattern to count the words in a line of text is to split the line into words and
#loop through the words and use a dictionary to track the count of each word independently.
""" from collections import Counter
counts=dict()
line=input('Enter a line of text: ')
words=line.split()
print(words) """
#Finding the maximum time a word occured using Counter
# word_count = Counter(words)
# print(word_count.most_common(1)[0])
""" for word in words:
    if(word is '.'): continue
    counts[word]=counts.get(word,0)+1
print(counts)
for key in counts:
    print(key)
    print(counts[key])
#Finding the maximum time a word occured
most_frequent=max(counts,key=counts.get)
print(most_frequent) """

#Printing the total-
# key=list(counts.keys())
# print(key)
# total=0
# for i in range(len(key)):
#     total=counts[key[i]]+total
# print(total)

""" 
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

"""
""" fname=input("Enter the name of file you want to open: ")
if len(fname)<1:
    fname='mbox-short.txt'

fh=open(fname,'r')
counts=dict()
for line in fh:
    line=line.strip()
    if not line.startswith('From '): continue
    person=line.split()[1]
    counts[person]=counts.get(person,0)+1
print(counts)
# max_frequent=max(counts,key=counts.get)
# print(f"{max_frequent} {counts[max_frequent]}")
bigWord = None
bigCount = None
for email,count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord=email
        bigCount=count

print(f"{bigWord}:{bigCount}")
 """

