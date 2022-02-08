import requests
import json

cidade = input('Escreva a sua cidade : ')

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade+'&appid=36b99c7d50372a4770fa890a22d667cb')

tempo = json.loads(requisicao.text)

print('Condição do tempo: {} '.format(tempo['weather'][0]['main']))
print('Temperatura: {:.1f} '.format(float(tempo['main']['temp']) - 273.15 ))