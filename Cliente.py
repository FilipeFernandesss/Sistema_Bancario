#class cliente

class Cliente():

    def __init__(self, nome, identidade, doc_identi, nacionalidade):
        self.nome = nome
        self.identidade = identidade
        self.doc_identi = doc_identi
        self.nacionalidade = nacionalidade
        self.controle_arquivo()

    def get_nome(self):
        return self.nome

    def get_identidade(self):
        return self.identidade

    def get_doc_identi(self):
        return self.doc_identi

    def get_nacionalidade(self):
        return self.nacionalidade

    def controle_arquivo(self):
        arquivo = open('cliente.txt', 'a')

        arquivo.write(self.get_nome() + ' - ')
        arquivo.write(self.get_identidade() + ' - ')
        arquivo.write(self.get_doc_identi() + ' - ')
        arquivo.write(self.get_nacionalidade() + '\n\r')

        arquivo.close()