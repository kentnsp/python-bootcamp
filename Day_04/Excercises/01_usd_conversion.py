import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")

if response.status_code == 200:
        conversion = response.json()

        print(conversion['rates']['USD'], "USD = ",conversion['rates']['PHP'], "PHP")


else:
        print("Failed. Server said:", response.status_code)