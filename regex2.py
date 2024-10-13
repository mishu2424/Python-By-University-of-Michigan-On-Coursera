#DOT(.) character
#--> It matches any character
#If you add Asterisk(*) after that it will match any character afterwards.
#For example-
import re
# a_str="X-Sieve: CMU Sieve\
# X-DSPAM-Result: Innocent\
# X-DSPAM-Confidence: 0.8475"
# str=re.findall('^X.*:',a_str)
# print(str)
fh=open('regex1.txt','r')
pattern = r'^(X-\S*:)'
for line in fh:
    line=line.strip()
    #re.search() returns a True/False depending on whether the string matches the regular expression.
    #If we actually want the matching strings to be extracted,we use re.findall()
    print(re.findall(pattern,line))
    if re.search(pattern,line):
        print(line)

x='My 2 favorite numbers are 19 and 42'
print(re.findall('\d+',x))

#Greedy Matching-
#-->The repeat characters(* and +) push outward in both directions(greedy) to match the largest possible string.
#For example-
a='From: Using the: charcater'
#Now if we want to extract just the 'From:' out of the text-
print(re.findall('F.+:',a)) #This would print up to 'From: Using the:' as this pattern also matches this. It extracted beyond what we wanted and this is called greedy matching.
#But to get just 'From:' out of it we will use the non-greedy character ?
print(re.findall('F.+?:',a))

b='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
print(re.findall('\S+@+\S+',b))


#Extracting the host name (uct.ac.za) using find and string slicing-
atpos=b.find('@')
epos=b.find(' ',atpos)
print(b[atpos+1:epos])
#Using double split pattern-
c=b.split()[1].split('@')[1]
print(c)
#Now using regex-
print(re.findall('@(\S+)',b))
# or
print(re.findall('@([^ ]+)',b)) #[^ ] everything but space.

numlist=list()
with open('mbox-short.txt','r') as file:
    for line in file:
        line=line.strip()
        stuff=re.findall("^X-DSPAM-Confidence: ([0-9.]+)",line)
        if len(stuff) !=1: continue
        numlist.append(float(stuff[0]))
print(f"Maximum: {max(numlist)}")