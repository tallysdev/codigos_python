lista = ['Gol', 'Uno', 'Palio',
'EcoSport', 'Clio', 'Strada', 'Golf']
arq = open('carros.txt', 'w')
for carro in lista:
 arq.write(carro + '\n')
arq.close()
