""" 
Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.

"""

""" fname=input("Enter the file name: ")
try:
    fhandle=open(fname)
except:
    print("File doesn't exist")
    quit()

for line in fhandle:
    line=line.rstrip()
    print(line.upper())
 """

""" 
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""
fname = input("Enter file name: ")
fh = open(fname)
lines=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line=line.strip()
    lines+=1
    print(line)
    confidence_value = float(line.split(":")[1].strip())
    total+=confidence_value

print(f"Average spam confidence: {total/lines}")
fh.close()
print("Done")