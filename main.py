#importaçoes
from Conta import Conta
from Cliente import Cliente
from conta_fisica import ContaFisica
from conta_juridica import ContaJuridica
from cartao_credito import Cartao_Credito
from cartao_debito import Cartao_Debito


#obejto conta fisica

cliente = Cliente('João','7894525', '458.485.987-42', 'Brasileiro')

conta_fisica = ContaFisica('124-875', '5412.55', 'Conta fisica','4578.54','qts25', cliente)
print(conta_fisica)
print(conta_fisica.get_cliente())
print()


#objeto conta juridica

cliente_juridica = Cliente('Teste A', '879453', '457.451.657-78', 'Brasileiro')
conta_juridica = ContaJuridica('N4561', '2145', 'Conta Juridica', cliente_juridica)

print(conta_juridica.infor_conta())
conta_juridica.deposito(150)
print(conta_juridica.infor_conta())

#Cartao de crédito
c1 = Cartao_Credito(conta_fisica, '7845', 789, '22/2025')
print(c1.senha)
c1.mudar_senha('Nova senha 123')
print(c1.senha)
print(c1.conta.get_saldo())
c1.conta.deposito(150)
print(c1.conta.get_saldo())
c1.conta.saque(140)
print(c1.conta.get_saldo())

c1.credito(150, 0)

#Cartão de débito
print()
cartao_d = Cartao_Debito(conta_fisica,'12345', 456, '22/2023')
cartao_d.conta.deposito(148)
print(cartao_d.debito(150))