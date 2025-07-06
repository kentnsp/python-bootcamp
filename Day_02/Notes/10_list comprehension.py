requests= {
    "Andrew":10,
    "Paddy": 21,
    "Alex": 30
}
banned = {"Alex"}

adults = []
for name, age in requests.items():
    if age >= 18:
        adults.append(name)

print(adults)

adults = [name for name, age in requests.items() if age >=18]
print('New: ', adults)

allowed = [name for name in adults if name not in banned]
print('allowed: ', allowed)