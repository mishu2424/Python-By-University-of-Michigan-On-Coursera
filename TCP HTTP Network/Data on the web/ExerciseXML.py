# http://py4e-data.dr-chuck.net/comments_42.xml 
import urllib.request, xml.etree.ElementTree as ET

url=input("Enter the URL: ")
if len(url) < 1:
    # url="http://py4e-data.dr-chuck.net/comments_42.xml"
    url="http://py4e-data.dr-chuck.net/comments_2097097.xml"
data=urllib.request.urlopen(url).read()
tree=ET.fromstring(data)

lst=tree.findall('comments/comment')
sum=0
count=0
for item in lst:
    sum+=int(item.find('count').text)
    count+=1
print(f"Sum: {sum}, Count: {count}")