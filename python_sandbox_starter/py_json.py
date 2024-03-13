# JSON is commonly used with data APIS. Here's how we can parse JSON into a Python dictionary
import json

#Convert a JSON to a dictionary => equivalent to JSON.parse() in JS.
userJSON = '{"first_name": "Jane", "last_name": "Doe", "age": 30}'
user = json.loads(userJSON) #Parse to a dict
print(user)
print(user['first_name'])

#Convert a dictionary to JSON => equivalent to JSON.stringify() in JS.
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)
print(carJSON)
