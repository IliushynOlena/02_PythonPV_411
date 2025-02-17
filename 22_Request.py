import requests

url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'

response = requests.get(url).json()
print(response)
print(type(response))
usd_buy = response[1]['buy']
usd_sale = response[1]['sale']
print(usd_buy)
print(usd_sale)