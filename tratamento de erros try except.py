import time

def abrir_arquivo():
    try:
        arquivo = open('algumarquivo.txt')
        return True
    except Exception as erro:
        print('Aconteceu algum erro:', erro)
        return False

while not abrir_arquivo():
    print('Tentando abrir o arquivo')
    time.sleep(5)

print('Abriu o arquivo!')

