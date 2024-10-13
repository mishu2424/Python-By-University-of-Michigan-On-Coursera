# We just took a look at the transport protocol, which is the lowest end layer in the TCP/IP stack. 
# We wrote a Python program and in that Python program we made a connection with the socket and then connected to a particular port on a far away computer,
# and now we're going to actually start sending data back and forth.
# There are rules that describe how we talk to them.
# The protocol that we're going to play with in this segment is what's called the hypertext transport protocol, or the hypertext transfer protocol.
#Suppose you are on a specific web page, where it says you can got to second page using a link-
#If you click on that link what happens behind the scenes-
"""

The browser is a piece of software running on your computer and it intercepts that click and it says, you've clicked on something. It looks at what's in the HTML of the page that you're coming from to say what web server to connect to, what port to connect to on that web server, and then what document to retrieve. Your browser then makes a socket connection to port 80(When you access a website using a URL that starts with http://, your browser automatically connects to port 80 on the server unless another port is specified) and sends a request called the get request, and sends that get request to port 80.
Then it goes in that web server and the web server parses that request and figures out what document you're looking for. It might run a little bit of software, but when it's all said and done, it produces on that same socket, a response. It sends that response back and that response back is in the form of HTML, the hypertext markup language, which is really tags inside less than and greater than pairs. That h1 says that it's a tender 1, p says it's the start of a paragraph, and then the a tag says that this is an anchor, and so it's supposed to be clickable text on that next page.
Then that comes back and your browser reads that, and then makes the page show up. It reads the HTML, parses it.

"""
#So, how can we do all this in Python -
#Importing socket module
import socket
#Telling socket which internet version to use, secondly choosing the type of socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Making connection
mysock.connect(('data.pr4e.org',80))
#Making a get request
#encode() turns unicode(strings) into UTF-8
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#sending what we want
mysock.send(cmd)

try:
    while True:
        #Recieving what we wanted
        data=mysock.recv(512)
        if len(data)<1:
            break
        #decode() does the opposite of encode(), turns the UTF-8 into Unicode.
        print(data.decode())

except:
    print("Something went wrong!")
mysock.close()


#Retreiving the web page using urllib
#Basically doing the same of what the code above does but with simple commands using urllib.
import urllib.request,urllib.parse,urllib.error

fhandle=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts=dict()
for line in fhandle:
    words=line.decode().strip().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)




##Now to get the HTML file-
fhandle=urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
for line in fhandle:
    print(line.decode().strip())