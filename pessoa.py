class Pessoa:
    # pass
    ''' 
    # as variaveis são declaradas no construtor
    nome = ""
    cpf = ""
    data_nascimento = ""
    '''
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        #self.cpf = cpf

    #como é dentro de uma classe, tem o parametro self
    def andar(self):
        print("A pessoa começou a caminhar...")

    #como é dentro de uma classe, tem o parametro self
    def comer(self):
        print("A pessoa está comentdo...")
    
    #como é dentro de uma classe, tem o parametro self
    def dormir(self):
        print('zzzzzzzzzzzzzzz')

class PessoaFisica(Pessoa):
    
    def __init__(self, nome, data_nascimento,cpf=None):
        self.cpf = cpf
        super().__init__(nome, data_nascimento)
    
    #como é dentro de uma classe, tem o parametro self
    def validar_cpf(self):
        if len(self.cpf) == 14:
            print("CPF Válido!")
        else:
            print("CPF Inválido!")
    def andar(self):
        print("A pessoa está andando a partir da classe PF")

class PessoaJuridica(Pessoa):
    
    def __init__(self, nome, data_nascimento, cpf, cnpj):
        self.cpf = cpf
        self.cnpj = cnpj
        super().__init__(nome, data_nascimento)
    
    def validar_cnpj(self):
        if len(self.cnpj) == 18:
            print("CNPJ Válido!")
        else:
            print("CNPJ Inválido!")