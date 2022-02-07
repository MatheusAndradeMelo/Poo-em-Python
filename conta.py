class Conta:

    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, quant):
        if quant > 0:
            self.saldo += quant
            print('Depósito concluído com sucesso!')
        else:
            print('Erro no depósito!')

    def consulta_saldo(self):
        return self.saldo

    def sacar(self, quant):
        if self.saldo - quant < 0:
            print('Você não possui saldo suficiente para o saque!')
        else:
            self.saldo -= quant
            print('Saque concluído com sucesso!')