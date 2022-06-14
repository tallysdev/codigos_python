# 2. A amplitude de um conjunto de .dados é uma medida estatística de dispersão definida como
# sendo a diferença entre o maior e o menor dentre os valores existentes nesse conjunto de
# dados. Escreva um programa em Python que leia uma sequência de k valores inteiros e
# armazene-os em uma lista. Em seguida, o programa deve calcular e exibir a amplitude desse
# conjunto de dados. O valor de k deve ser definido pelo usuário no início do programa.

ampli = []
n = int(input('Deseja adicionar quantos dados na lista?\t'))
for i in range(n):
    a = int(input('informe o valor:\t'))
    ampli.append(a)

ampli.sort()

b = ampli[0] - ampli[n-1]

print(' a ampliude dos valores foi;\t',b)