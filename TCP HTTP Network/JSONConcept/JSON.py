import json

data= """{
   "name":"Mishu",
   "phone":{
      "type":"intl",
      "number": "+1 734 303 4456"
   },
   "email": {
      "hide":"yes"
   }
}"""

info=json.loads(data)
print(f"Name: {info["name"]} and Phone number: {info["phone"]["number"]} and Hide: {info["email"]["hide"]}")


input=""" [
    {
      "id" : "001",
      "x" : "2",
      "name": "Mishu"
    },
    {
      "id" : "009",
      "x" : "7",
      "name" : "Barsha"
    }

]
"""
info2=json.loads(input)
print(info2)
for item in info2:
    print(f"Name: {item["name"]} and ID: {item["id"]} and x: {item["x"]}")