#class cliente

class Cliente():

    def __init__(self, nome, identidade, doc_identi, nacionalidade):
        self.nome = nome
        self.identidade = identidade
        self.doc_identi = doc_identi
        self.nacionalidade = nacionalidade

    def get_nome(self):
        return self.nome

    def get_identidade(self):
        return self.identidade

    def get_doc_identi(self):
        return self.doc_identi

    def get_nacionalidade(self):
        return self.nacionalidade

