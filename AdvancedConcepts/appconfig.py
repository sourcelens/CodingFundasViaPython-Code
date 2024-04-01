#appconfig
import yaml


with open('config.yml', 'r') as file:
    prime_service = yaml.safe_load(file)

print(prime_service['prime_numbers'][0])
print(prime_service['rest']['url'])


import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])