import requests
import json

url_base = "https://economia.awesomeapi.com.br/last/"

def cotar_moeda():
    moeda = "BRL-USD"
    url_final = url_base + moeda
    response = requests.get(url_final)
    content_json = response.json()
    return content_json

def testar_conexao(url):
    status_code = requests.get(url).status_code
    if status_code != 200:
        return False
    return True

print(testar_conexao("https://google.com.br"))