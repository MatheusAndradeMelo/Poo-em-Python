import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = json.loads(requisicao.text)

    print('=' * 10,'COTAÇÃO','=' * 10, datetime.datetime.now())
    #print('Dólar : U$',cotacao)
    print('Dólar : U$',cotacao['USDBRL']['high'])
    print('Euro : U$',cotacao['EURBRL']['high'])
    print('BTC : U$', cotacao['BTCBRL']['high'])
    time.sleep(30)
