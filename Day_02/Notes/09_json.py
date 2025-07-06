import json
data =[
    {"Name":"Alice", "Age": 30},
    {"Name":"Ken", "Age": 27}
]

with open('people.json','w') as file:
    json.dump(data, file, indent=4)