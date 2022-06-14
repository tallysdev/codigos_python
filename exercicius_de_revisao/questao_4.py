# 4. Simule a execução do programa abaixo em um interpretador Python, analisando o valor de
# cada variável em cada linha do programa. Simule a tela de execução do programa,
# mostrando os valores que serão exibidos cada vez que a função print() é chamada.

lista = [56, 89, 12, 87, 43]
print ('Lista Inicial: ',lista)
aux = []
tam = len (lista)
while lista != [] :
    aux.append (lista [tam-1])
    del lista[tam-1]
    tam -= 1
    print (aux)
tam = len (aux)
for i in range (tam):
    lista.append (aux [i]) 
print ('Lista Final :',lista)