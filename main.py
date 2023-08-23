import requests

# accessing api
response = requests.get("https://open.er-api.com/v6/latest/USD")
json_data = response.json()
json_rates = json_data['rates']

# changing currency amount to USD
abb1 = input("enter first rate abbreviation: ").upper()
amount = float(input("enter amount to exchange: "))
currency1 = json_rates[abb1]
money = amount/currency1

# money times new currency
abb2 = input("enter rate abbreviation to convert to: ").upper()
currency2 = json_rates[abb2]
new = money*currency2
print(str(amount)+" "+abb1+" is: "+str(new)+" "+abb2)

