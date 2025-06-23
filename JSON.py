import json
data = {
    'person':{
        "name":"Madhansai",
        "age":22
    },
    "student":{
        "name":"Ebron",
        "age":22,
    }
}

with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\ex.json",'w')as f:
    json.dump(data,f,indent=2)

with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\ex.json",'r')as f:
    data = json.load(f)
print(data["person"])
print(data["student"])




with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\ex.json",'r') as file:
    data = json.load(file)

print(data)



json_string = '{"name": "John", "age": 30, "city": "New York"}'


data = json.loads(json_string)

print(data)


data = {
    "name": "Alice",
    "age": 25,
    "city": "Boston",
    "skills": ["Python", "SQL", "Machine Learning"]
}

with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\ex.json",'w') as file:
    json.dump(data, file, indent=4)



data = {
    "name": "Bob",
    "age": 40,
    "city": "Chicago"
}


json_string = json.dumps(data, indent=2)
print(json_string)
