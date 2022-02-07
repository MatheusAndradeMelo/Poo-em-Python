from cliente import Cliente
from conta import Conta

print('=' * 10, 'CLIENTE', '=' * 10)

cliente1 = Cliente('Matheus', '17480005784', 22)

print(cliente1)

print('=' * 10, 'CONTA DO BANCO', '=' * 10)

conta1 = Conta(cliente1, 2500)

print('O cliente', conta1.cliente.nome, ', possui : R$', conta1.consulta_saldo(),', de saldo no banco.')

conta1.depositar(500)

print('Após o depósito seu saldo é de : R$', conta1.consulta_saldo())

conta1.sacar(300)

print('Após o saque seu saldo é de : R$',conta1.consulta_saldo())