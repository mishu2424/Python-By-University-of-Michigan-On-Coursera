#Tuples are another kind of sequence that functions much like a list 
#except for the fact that you can't modify anything in the tuple.(immutable)
#They have elements which are indexed starting at 0.

x=('Glenn','Max','Joseph')
print(x[2])
for iter in x:
    print(iter)
#But you can't do it-
# x[1]='Gamini' 
#But you can store list, set/dictionaries in the tuples which are mutable.
#So, meaning- Even though the tuple itself can’t change, the contents of those mutable items can be modified. 
y=([2,3],{2,3},{'Hector':2})
print(y)
y[0][1]=2
print(y)
print(y[2]['Hector'])
#n summary, a tuple itself can’t be changed, but it can hold items that can be changed (like lists or dictionaries). If those items are immutable (like strings or other tuples), you can't change them either.
#Using max() function
a= ( 1, 9, 2)
print(max(a))

#Only two methods for tuples-
#count,index

#Tuples are more efficient in the sense that since Python does not have to build
#tuple structures to be modifiable, they are simpler and more efficient
#in terms of memory use and performance than lists

#So in our program when we are making "temporary variables" we prefer tuples over lists.

#Tuples and Assignment
#-->We can also put a tuple on the left-hand side of an assignment statement
#-->We can even omit the parentheses
(b,c)=(94,'fred')
print(b,c)
#swapping-
d,e=4,5
(d,e)= (e,d)
print(d,e)