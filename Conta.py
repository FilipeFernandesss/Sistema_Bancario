#classe conta (Mãe)
class Conta:

    #construtor
    def __init__(self, numero, agencia, tipo):
        self.numero = numero
        self.agencia = agencia
        self.tipo = tipo

    def get_numero(self):
        return self.numero

    def get_agencia(self):
        return self.agencia

    def get_tipo(self):
        return self.tipo