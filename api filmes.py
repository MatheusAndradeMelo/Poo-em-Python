import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=9b33ea0c' + titulo)
        texto = req.text
        print('Requisição aceita!')
        dicionario = json.loads(texto)
        return dicionario
    except Exception as erro:
        print('Requisição inválida!')
        return None

def printar_detalhes(filme):
    # print(dicionario)
    print('Titulo: ', filme['Title'])
    print('Atores: ', filme['Actors'])
    print('Diretor: ', filme['Director'])
    print('Ano: ', filme['Year'])
    print('')

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')
    if op == 'SAIR':
        sair = True
        print('Você saiu do programa! Até a próxima!')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado!')
        else:
            printar_detalhes(filme)
