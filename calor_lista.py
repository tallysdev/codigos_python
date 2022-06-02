# Escreva um programa em Python que leia e
# armazene 6 valores de temperatura, obtidos
# a partir do teclado. Em seguida, o programa
# deve exibir na tela a lista de temperaturas nas
# seguintes formas:
# a) Na mesma ordem em que foram lidos do
# teclado
# b) Na ordem inversa à que foram lidos do
# teclado
# c) Ordenados em ordem crescente
# d) Ordenados em ordem decrescente
tempe = []
quant = int(input('Quanto valores de temperatura voce ira guardar?\n'))
for i in range(quant):
    temp = input('informe a temperatura no tempo {}:\t' .format(i + 1))
    tempe.append(temp)

print('\n')
# a)
print(tempe,'\n')
# b)
newtempe = list(reversed(tempe))
print(newtempe,'\n')
# c)
print(sorted(tempe),'\n')
# d)
tempe.sort(reverse=True)
print(tempe,'\n')