# item = {
#     "Name": "Switch2",
#     "Info": "Console",
#     "Cost": "Php 40,000",
#     "Warranty": "1 Year",
#     "Memory": "256 GB"
# }
#
# print("Item:")
# for key, value in item.items():
#     print("\t",key,":", value)

wishlist = [
     {
        "Name": "Switch2",
        "Info": "Console",
        "Cost": "Php 40,000",
        "Warranty": "1 Year",
        "Memory": "256 GB"
    },
    {
        "Name": "Samsung Galaxy",
        "Info": "Smartphone",
        "Cost": "Php 50,000",
        "Warranty": "2 Years",
        "Memory": "128 GB"
    },
    {
        "Name": "iPhone",
        "Info": "Smartphone",
        "Cost": "Php 60,000",
        "Warranty": "5 Years",
        "Memory": "256 GB"
    }
]

for index, order in enumerate(wishlist, start=1):
    print("Item:", index)

    for key, value in order.items():
        print(f"\t{key} : {value}")

    print()