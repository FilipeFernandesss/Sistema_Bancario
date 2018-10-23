#Cartao de débito

from Cartao import Cartao

class Cartao_Debito(Cartao):
    def __init__(self, conta, numero, codigo_seguranca, data_vencimento):
        super().__init__(conta, numero, codigo_seguranca, data_vencimento)

        self.conta = conta
        self.nome = conta.cliente.get_nome()
        self.numero = numero
        self.codigo_seguranca = codigo_seguranca
        self.data_vencimento = data_vencimento
        self.senha = None

    #Método debito
    def debito(self, compra):
        if compra <= self.conta.get_saldo():
            self.conta.saldo -= compra
            return self.conta.saldo
        else:
            return f'Saldo insuficiente para realizar a transição!' \
                   f'\nSaldo de: ${self.conta.saldo}\nValor da compra: ${compra}'
