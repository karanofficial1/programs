import json

# Convert from JSON to Python:

# some JSON:
x =  '{ "name":"Karan", "age":30, "city":"Mahendra Nagar"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y)

# Convert from Python to JSON:
# a Python object (dict):
x = {
  'name': "KARAN",
  "age": 30,
  "city": "Kanchanpur"
}
# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# Convert Python objects into JSON strings, and print the values:
print(json.dumps({"name": "Karan", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



# Convert a Python object containing all the legal data types:
x = {
  'name': "Karan",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Pratik","Dhami"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", 'mpg': 24.1}
  ]
}

print(json.dumps(x))
print(25*'-')

y = json.dumps(x, indent=4, separators=(". ", " = "))
print(y)


print(json.dumps(x, indent=4, sort_keys=True))