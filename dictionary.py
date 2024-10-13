#Comparing dictionary and list
# Doctionaries are like lists except that they use keys instead of numbers to look up values.
#list
lst=list()
lst.append(12)
lst.append(5)
print(lst)
lst[0]=25
print(lst)  

#dictionary
ddd=dict()
ddd['name']='Mishu'
ddd['age']=24
print(ddd)
print(ddd['name'])
ddd['age']=23
print(ddd)