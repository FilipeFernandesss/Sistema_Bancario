#classe conta (Mãe)
class Conta:

    #construtor
    def __init__(self, numero, agencia, tipo, saldo=0):
        self.numero = numero
        self.agencia = agencia
        self.tipo = tipo
        self.saldo = saldo

    def get_numero(self):
        return self.numero

    def get_agencia(self):
        return self.agencia

    def get_tipo(self):
        return self.tipo

    def get_saldo(self):
        return self.saldo

    # Método depósito
    def deposito(self, valor):
        self.saldo += valor

    #Método saque
    def saque(self, valor):
        if valor < self.get_saldo():
            self.saldo -= valor
            print(f"Saque de ${valor} efetuado com sucesso")
        else:
            print("Saque não efetuado")