#Conta jurididca

from Conta import Conta


class ContaJuridica(Conta):
    def __init__(self, numero, agencia, tipo, cliente, saldo=0):

        #Heranca da classe Conta
        super().__init__(numero, agencia, tipo, saldo)

        #Atributos do cliente
        self.empresa = cliente.get_nome()
        self.identidade_dono = cliente.get_identidade()
        self.cnpj = cliente.get_doc_identi()
        self.nacionalidade = cliente.get_nacionalidade()

        #Iniciando o saldo zerado e o status
        self.disponivel = True
        self.saldo = saldo

    #Métodos GETS
    def get_empresa(self):
        return self.empresa

    def get_iden_dono(self):
        return self.identidade_dono

    def get_cnpj(self):
        return self.cnpj

    def get_nacionalidade(self):
        return self.nacionalidade

    def get_disponivel(self):
        return self.disponivel

    # Informações da conta
    def infor_conta(self):
         return f'Nome: {self.empresa}\nCNPJ: {self.cnpj}\nSaldo: {self.saldo}'

    def __str__(self):
        return f'Empresa: {self.empresa}\nIdentidade: ' \
               f'{self.identidade_dono}\nCnpj: {self.cnpj}\nNacionalidade: {self.nacionalidade}' #falta terminar
