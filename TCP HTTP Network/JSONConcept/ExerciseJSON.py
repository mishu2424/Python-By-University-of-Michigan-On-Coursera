# https://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_2097098.json
import urllib.request,urllib.parse, json

url=input("Enter the URL: ")
data=urllib.request.urlopen(url).read().decode()
js=json.loads(data)
counts=js['comments']
sum=0
for count in counts:
    sum+=count['count']
print(sum)