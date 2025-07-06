import json

with open('wishlist.json','r') as file:
    data = json.load(file)

    print(data)