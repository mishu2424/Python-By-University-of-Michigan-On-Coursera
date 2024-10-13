#importing the library and modules-
# import urllib.request, urllib.parse, urllib.error, re
# from bs4 import BeautifulSoup

# def parsing(url):
#     html= urllib.request.urlopen(url).read()
#     soup=BeautifulSoup(html,'html.parser')
#     return soup
# soup=parsing('http://py4e-data.dr-chuck.net/known_by_Fikret.html')
# # soup=parsing('http://py4e-data.dr-chuck.net/known_by_Roslin.html')
# tags=soup('a')
# # print(tags)
# for tag in tags:
#     print(tag.get('href',None))


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
# url = input("Enter URL : ")

# position = int(input("Enter the position - ")) - 1
# count = int(input("Enter the count - "))
# count2 = 0
# while(count2 < count):
#     html = urllib.request.urlopen(url).read()
#     soup = BeautifulSoup(html, 'html.parser')

#     tags = soup('a')
#     url = tags[position].get('href')
#     name = tags[position].contents[0]
#     count2+=1

# print(name)

# list_tags=list(tags)
# print(list_tags[2])
# for i in range(len(list_tags)):
#     if i==2:
#         print(list_tags[i])

# for tag in tags:
#     if tag.string=='Kayley':
#         url=tag.get('href',None)
#         newSoup=parsing(url)
#         all_tags=newSoup.find_all('a',limit=8)
#         # for a_tag in all_tags:
#         #     print(a_tag.string)      
#         print(all_tags[7].string)
#     continue


pos=int(input("Enter position: "))-1
count=int(input("Repeat times: "))
url='https://py4e-data.dr-chuck.net/known_by_Roslin.html'
while count:
    html = urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup.find_all('a')
    url=tags[pos].get('href',None)
    name=tags[pos].text
    count-=1
print(name)
 
