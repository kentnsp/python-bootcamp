import json

wishlist = [
     {
        "Name": "Switch2",
        "Info": "Console",
        "Cost": 40_000,
        "Warranty": "1 Year",
        "Memory": "256 GB"
    },
    {
        "Name": "Samsung Galaxy",
        "Info": "Smartphone",
        "Cost": 50_000,
        "Warranty": "2 Years",
        "Memory": "128 GB"
    },
    {
        "Name": "iPhone",
        "Info": "Smartphone",
        "Cost": 60_000,
        "Warranty": "5 Years",
        "Memory": "256 GB"
    }
]

with open('wishlist.json','w') as file:
    json.dump(wishlist, file, indent=4)



