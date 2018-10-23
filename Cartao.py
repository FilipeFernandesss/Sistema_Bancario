# Classe mae dos cartoes
class Cartao:
    #Método construtor
    def __init__(self, conta, numero, codigo_seguranca, data_vencimento):
        self.proprietario = conta
        self.conta = conta
        self.numero = numero
        self.codigo_seguranca = codigo_seguranca
        self.data_vencimento = data_vencimento
        self.senha = None

    #Métodos GETS
    def get_proprietario(self):
        return self.proprietario

    def get_numero(self):
        return self.numero

    def get_codigo_seguran(self):
        return self.codigo_seguranca

    def get_data_venc(self):
        return self.data_vencimento

    def get_senha(self):
        return self.senha

    #Método para mudar a senha
    def mudar_senha(self, nova_senha):
        self.senha = nova_senha
