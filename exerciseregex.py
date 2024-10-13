# import re
# sum=0
# count=0
# lst=list()
# with open('exerciseregex.txt','r') as file:
#     for line in file:
#         line=line.strip()
#         numbers=re.findall(r'[0-9]+',line)
#         if len(numbers) >0: 
#             for number in numbers:
#                 sum+=int(number)
#                 count+=1
# print(sum,count)

#Solving same problem using list comprehension
import re

with open('exerciseregex.txt', 'r') as file:
    numbers = [int(num) for line in file for num in re.findall(r'\d+', line.strip())]

print(numbers, sep='\n')  # Print each number on a new line
print(f"Sum: {sum(numbers)}, Count: {len(numbers)}")