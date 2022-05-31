# adicioando valores na lista
from random import randint, random


lista = []
lista1 = lista + [10]
lista1 += [20]
lista1.append(30)
# print(lista1)

# modificando lista
vetor = [1,2,3,4,5,6]
# print('lista primaria')
# print(vetor)
vetor[0] = 7
# print('lista modificada')
# print(vetor)

# gerando numeros para colocar na lista mega, (obs: igual o da mega-sena) 
mega = []
contador = 0
ndez= int(input('Quantas dezenas? (6-10)'))
while contador < ndez:
    numeros = randint(1,60)
    if numeros not in mega:
        mega.append(numeros)
        contador+=1

mega.sort()
print(mega)