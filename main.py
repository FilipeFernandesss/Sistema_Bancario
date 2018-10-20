#importaçoes
from Conta import Conta
from Cliente import Cliente
from conta_fisica import ContaFisica
from conta_juridica import ContaJuridica


#obejto conta fisica

cliente = Cliente('João','7894525', '458.485.987-42', 'Brasileiro')

conta_fisica = ContaFisica('124-875', '5412.55', 'Qst25','4578.54','qts25', cliente)
print(conta_fisica)
print(conta_fisica.get_cliente())
print()


#objeto conta juridica

cliente_juridica = Cliente('Teste A', '879453', '457.451.657-78', 'Brasileiro')
conta_juridica = ContaJuridica('N4561', '2145', 'Conta Juridica', cliente_juridica)

print(conta_juridica.infor_conta())
conta_juridica.deposito(150)
print(conta_juridica.infor_conta())