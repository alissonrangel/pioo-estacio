'''
# diminuirá a performance
import pessoa # todas as classes já estarão disponíveis
'''
#menor consumo de memória
from pessoa import PessoaFisica, PessoaJuridica # Somente a classe Pessoa poderá ser usada

pf1 = PessoaFisica("Pessoa Física Nova", "23/09/1990", "12.456.789-09")

print('Dados da PF1')
print('Nome: ', pf1.nome)
print('CPF: ', pf1.cpf)
print('Data nascimento: ', pf1.data_nascimento)
pf1.andar()
pf1.comer()
pf1.dormir()
pf1.validar_cpf()

pj1 = PessoaJuridica("Francisco André", "22/03/1970","123.987.675-00", "12.000.000/0001-00")

print('Dados da PJ1')
print('Nome: ', pj1.nome)
print('CPF: ', pj1.cpf)
print('Data nascimento: ', pj1.data_nascimento)
pj1.validar_cnpj()






'''
p1 = Pessoa("Francisco André", "28/06/1981", "123.456.789-09") # ou p1 = Pessoa
#p1 = Pessoa()
#p1.nome = "Francisco André"
#p1.cpf = "123.456.789-09"
#p1.data_nascimento = "28/06/1981"
p1.nome_mae = "Mamãe da p1"

print('Dados da P1')
print('Nome: ', p1.nome)
print('CPF: ', p1.cpf)
print('Data nascimento: ', p1.data_nascimento)
print('Nome mãe: ', p1.nome_mae)
'''

'''
p2 = Pessoa() # ou p1 = Pessoa

p2.nome = "Uma nova pessoa"
p2.cpf = "234.876.478-09"
p2.data_nascimento = "31/09/2003"

print('Dados da P2')
print('Nome: ', p2.nome)
print('CPF: ', p2.cpf)
print('Data nascimento: ', p2.data_nascimento)

print("Endereço p1: ", id(p1))
print("Endereço p2: ", id(p2))

p3 = Pessoa()
p4 = Pessoa

print("Endereço p3: ", id(p3))
print("Endereço p4: ", id(p4))

print('Dados da P3')
print('Nome: ', p3.nome)
print('CPF: ', p3.cpf)
print('Data nascimento: ', p3.data_nascimento)
'''