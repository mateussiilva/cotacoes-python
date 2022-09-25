import json
import requests


url = 'https://economia.awesomeapi.com.br/last/BTC-BRL'

MOEDA = 'BTCBRL'

response = requests.get(url)
file_json = response.json()
print(file_json[MOEDA])