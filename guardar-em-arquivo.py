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


lista2.sort()

for carro in lista2:
 print(carro)

arq = open('carros.txt','w')

for carroa in lista2:
    arq.write(carroa + '\n')
arq.close()
