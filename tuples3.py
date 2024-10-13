#Sorting lists of tuples-
#--> We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary.
#First thing first, lets sort the dictionary by the key using the items() method and sorted() function

a={'a':10, 'c':22, 'b':1}
print(a.items())
print(sorted(a.items()))

#Using sorted() in loop
for k,v in sorted(a.items()):
    print(k,v)


#Sorting using values-
lst=list()
for key,value in a.items():
    lst.append((value,key))
print(lst)
print(sorted(lst,reverse=True))
#OR using the list comprehension-
print(sorted([(v,k) for k,v in a.items()],reverse=True))

#Finding the most 10 common words-
fh=open('romeo.txt','r')

dic=dict()
for line in fh:
    words=line.strip().split()
    for k in words:
           dic[k]=dic.get(k,0)+1
print(dic)
lst2=list()
""" for k,v in dic.items():
     lst2.append((v,k))
lst2=sorted(lst2,reverse=True)

print(lst2[:10])
for k,v in lst2[:10]:
     print(k,v) """

#OR using list comprehension-
print(sorted([(v,k) for k,v in dic.items()],reverse=True)[:10])