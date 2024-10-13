# import urllib.request, urllib.parse, urllib.error, ssl, json

# address=input("Enter the loaction: ").strip()
# serviceURL='http://py4e-data.dr-chuck.net/opengeo?'
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# parms=dict()
# parms['q']=address
# url=serviceURL+urllib.parse.urlencode(parms)
# print('URL:',url)
# data=urllib.request.urlopen(url, context=ctx).read().decode()
# # print(data)
# try:
#     js=json.loads(data)
# except:
#     js=None
# print(js['features'][0]['properties']["plus_code"])


import urllib.request, urllib.parse, urllib.error, json
address=input("Enter loaction: ").strip()
serviceURL='http://py4e-data.dr-chuck.net/opengeo?'
parms=dict()
parms['q']=address
url=serviceURL+urllib.parse.urlencode(parms)
data=urllib.request.urlopen(url)
js=json.load(data)
print(js)
print(type(js))
jsdumps=json.dumps(js,indent=4)
print('DUMPED JSON-')
print(jsdumps)
print(type(jsdumps))