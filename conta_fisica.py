#Conta Física

from Conta import Conta


class ContaFisica(Conta):
    def __init__(self, numero, agencia, tipo, compro_renda, compro_residen, cliente):
        #Heranca da classe Conta
        super().__init__(numero, agencia, tipo)
        #Atributos do cliente e da conta fisica
        self.cliente = cliente
        self.nome = self.cliente.get_nome()
        self.identidade = self.cliente.get_identidade()
        self.cpf = self.cliente.get_doc_identi()
        self.nacionalidade = self.cliente.get_doc_identi()
        self.compro_renda = compro_renda
        self.compro_residen = compro_residen
        # Iniciando o saldo da conta zerado e o status
        self.saldo = 0
        self.disponivel = True
        print('Conta criada')

    #Métodos GETS
    def get_compro_renda(self):
        return self.compro_renda

    def get_compro_residen(self):
        return self.compro_residen

    def get_cliente(self):
        return f'Nome: {self.nome}, Identidade: {self.identidade}, Cpf: {self.cpf}'

    def get_saldo(self):
        return self.saldo

    def get_disponivel(self):
        return self.disponivel

    #Método depósito
    def deposito(self, valor):
        if self.get_disponivel():
            self.saldo += valor

    #Informações da conta
    def infor_conta(self):
        return f'Nome: {self.nome}\nCpf: {self.cpf}\nSaldo: {self.saldo}'

    def __str__(self):
        return f'Nome: {self.nome}\nIdentidade: {self.identidade}\nCpf: {self.cpf}\nNacionalidade: {self.nacionalidade}'