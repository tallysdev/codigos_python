lista = ['Gol', 'Uno', 'Palio',
'EcoSport', 'Clio', 'Strada', 'Golf']
arq = open('carros.txt', 'w')
for carro in lista:
    arq.write(carro + '\n')
arq.close()


lista2 = []
arq = open('carros.txt', 'r')
for linha in arq:
    linha = linha.rstrip()
    lista2.append(linha)
arq.close()

arq = open('carros.txt','a')

arq.sort()

arq.close()

lista2.sort()
print('Lista de carros do arquivo:')
for carro in lista2:
 print(carro)
