#Tuples and Dictionaries
#--> The items() method in dictionaries returns a list of (key,value) tuples

d=dict()
d['csev']=2
d['cwen']=3
for k,v in d.items():
    print(k,v)

tups=d.items()
print(tups)

#Tuples are Comparable
#--> The comparison operators work with tuples and other sequences.
#--> If the first item is equal, Python goes on to the next element, and so on, until it finds elements that differ.
print((0,1,2)<(5,1,2)) # in this case, the compiler just checked the first item and returns True instead of checking each element.
print(( 0, 1, 20000)<( 0, 3, 4)) #in this case, as the first elements are equal, it goes to the second element and returns True. Didn't go to the third element.
print(('Jones','Sally')<('Jones','Sam'))
print(('Jones','Sally')>('Adams','Sam'))


