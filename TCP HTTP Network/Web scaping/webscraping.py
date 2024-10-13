#When a program or script pretends to be a browser and retrieves
# web pages, looks at those web pages, extracts information, and 
# then looks at more web pages.

# Search engines scrape web pages-we call this "spidering the web" or "Web crawling".
from bs4 import BeautifulSoup
import urllib.request,urllib.error,urllib.parse,re
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter URL- ").strip()
html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
print(soup.prettify())

tags=soup('a')
print(tags)
for tag in tags:
    print(tag.get('href',None)) #this get() method is not the one we use in dictionary, instead, it's method of Beautiful sopu itself.
# http://www.dr-chuck.com/page1.html