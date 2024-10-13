#importing urllib and beautiful soup
import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup
url=input('Enter the URL: ')
html=urllib.request.urlopen(url).read()
soup= BeautifulSoup(html,'html.parser')
# print(soup.prettify())
tags=soup.find_all('span')
# print(tags)
sum=0
count=0
for tag in tags:
    # print(tag.contents[0])
    # print(re.findall('<span.*>(\d+)<.*>',tag.decode()))
    value=int(tag.string)
    sum+=value
    count+=1
print(f"Count:{count} and Sum:{sum}")
    
# http://py4e-data.dr-chuck.net/comments_2097095.html