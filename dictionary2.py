#one common use of dictionaries is counting how often we 'see' something.
""" ccc=dict()
ccc['csev']=1
ccc['cwen']=1
print(ccc)
ccc['cwen']=ccc['cwen']+1
print(ccc) """

#Dictionary Tracebacks
# --> It is an error to reference a key which is not in the dictionary.
#--> We can use the in operator to see if a key is in the dictionary

""" ddd=dict()
ddd['bisev']=1
print(ddd) """
# print(ddd['kosev']) #This key doesn't exist. In this case, it will show an error.

#We can use the in operator to see if a key is in the dictionary.
#So to make sure we don't get tracebacks, we can use the in operator in such way-

""" if 'kosev' not in ddd:
    ddd['kosev']=3
else:
    ddd['kosev']=ddd['kosev'] +1

print(ddd)
 """
#We can use get() method for this-
""" val=ddd.get('kosev','Not found')
if val is 'Not found':
    ddd['kosev']=3
else:
    ddd['kosev']=ddd['kosev']+1
print(ddd) """
#Example-
counts={
    'csev':2,
    'cwen':2,
    'zqian':1
}

names=['csev','cwen','csev','zqian','cwen','lili']

for name in names:
    count=counts.get(name,'Not found')
    if count is "Not found":
        counts[name]=3
print(counts)
#Counting people-
counts=dict()
names=['csev','cwen','csev','zqian','cwen']

for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)