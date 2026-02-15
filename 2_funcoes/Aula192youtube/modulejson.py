import json
import os
# pessoas = [
# {
#     "name":"Luiz", 
#     "lastname":"Miranda", 
#     "age":22,
#     "addresses":[
#     {"Line1":"Av.brasik"},{"Line1":"Av.amapa"}]
# },
# {
#     "name":"Mario", 
#     "lastname":"Miranda", 
#     "age":22,
#     "addresses":[
#     {"Line1":"Av.brasik"},{"Line1":"Av.amapa"}]
# }
# ]


# BASE_DIR = os.path.dirname(__file__)
# SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

# with open(SAVE_TO,'w') as file:
#     json.dump(pessoas, file, indent=2)


# print(json.dumps(pessoas, indent=2))

# BASE_DIR = os.path.dirname(__file__)
# JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

# with open(JSON_FILE, 'r') as file:
#     pessoas = json.load(file)
#     print(json.dumps(pessoas))

    # for pessoa in pessoas:
    #     print(pessoa["name"])

json_string = """
[{"name": "Luiz", "lastname": "Miranda", "age": 22, "addresses": [{"Line1": "Av.brasik"}, {"Line1": "Av.amapa"}]}, {"name": "Mario", "lastname": "Miranda", "age": 22, "addresses": [{"Line1": "Av.brasik"}, {"Line1": "Av.amapa"}]}]
"""
pessoas = json.loads(json_string)

for pessoa in pessoas:
    print(pessoa['name'])