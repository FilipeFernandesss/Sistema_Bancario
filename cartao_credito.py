#Cartao de Crédito
from Cartao import Cartao

class Cartao_Credito(Cartao):
    def __init__(self, conta, numero, codigo_seguranca, data_vencimento):
        super().__init__(conta, numero, codigo_seguranca, data_vencimento)

        self.conta = conta
        self.nome = conta.cliente.get_nome()
        self.numero = numero
        self.codigo_seguranca = codigo_seguranca
        self.data_vencimento = data_vencimento
        self.senha = None

        #Método do txt
        self.controle_txt()

    #Método de controle txt
    def controle_txt(self):
        arquivo = open('cartao_credito.txt', 'a')

        arquivo.write(self.conta.cliente.get_nome() + ' - ')
        arquivo.write(self.get_numero() + ' - ')
        arquivo.write(str(self.get_codigo_seguran()) + ' - ')
        arquivo.write(self.get_data_venc() + ' - ')
        arquivo.write(str(self.get_senha()) + '\n\r')

        arquivo.close()


    #Método de crédito
    def credito(self, valor_compra, qtd_parcela):
        if qtd_parcela <=0:
            print("Algo incorreto ocorreu")
        else:
            valor_pagamento = valor_compra/qtd_parcela
            if qtd_parcela > 1:
                print('O pagamento da compra de $',valor_compra,'parcelada em ',qtd_parcela,
                      'vezes será de: {:.2f}'.format(valor_pagamento))
            else:
                print('O pagamento da compra de $', valor_compra, 'parcelada em ', qtd_parcela,
                      'vez será de: {:.2f}'.format(valor_pagamento))
