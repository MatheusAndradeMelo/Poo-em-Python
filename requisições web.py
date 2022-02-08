import requests

texto = None

try:
    requisicao = requests.get('http://g1.com.br')
    texto = requisicao.text
except Exception as erro:
    print('Requisicao deu erro:', erro)

print(texto)

