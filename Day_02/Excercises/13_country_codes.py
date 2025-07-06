country_codes = {
    "PH": "Philippines",
    "US": "United states",
    "JP": "Japan",
    "UK" : "United Kingdom",
}
print(country_codes)

country_code = input("Enter Country code: ")
#print(country_codes[country_code])
print(country_codes.get(country_code, "unknown"))

for key in country_codes:
    print("KEYS",key)

for value in country_codes.values():
    print("VALUES",value)

for key, value in country_codes.items():
    print("BOTH", key, value)