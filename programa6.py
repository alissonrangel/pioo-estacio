lista = ['string', 1, 5.1, True, tuple()] # é mutável
tupla = ('string', 1, 5.1, True, list()) # é imutável
dicionario = {'string':'palavra', '1' : 2, 5.1 : 6.2, True: False, False: True}
# conjunto = set()

print('Lista: ', lista)
print('Tupla: ', tupla)
print('Dicionário: ', dicionario)

lista.append(50)

print('Lista: ', lista[5])
print('Tupla: ', tupla[2])