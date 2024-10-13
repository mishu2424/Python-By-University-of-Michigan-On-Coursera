"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

"""

fh=open('mbox-short.txt','r')
dic=dict()
for line in fh:
    line=line.strip()
    if not line.startswith("From "): continue
    hours=line.split()[5].split(':')[0]
    print(hours)

    dic[hours]=dic.get(hours,0)+1
print(dic)
lst=list()
for k,v in sorted(dic.items()):
    print(k,v)
#Now using list comprehension-
print(sorted([(k,v) for k,v in dic.items()]))

""" 
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

"""

fName=input("Enter the file name: ")
if len(fName)<1:
    fName='mbox-short.txt'
fh=open(fName,'r')
counts=dict()
for line in fh:
    line=line.strip()
    if not line.startswith('From '): continue
    person=line.split()[1]
    counts[person]=counts.get(person,0)+1
print(counts)
# max_count=max(counts,key=counts.get)
# print(max_count)
lst=list()
for k,v in counts.items():
    lst.append((v,k))
print(lst)

sorted_lst=sorted(lst,reverse=True)
#Maximum-
print(sorted_lst[0])
print(sorted_lst[0][0])
#5 most count mail address-
for k,v in sorted_lst[:5]:
    print(k,v)
#List comprehension-
print(sorted([(v,k) for k,v in counts.items()],reverse=True)[:5])