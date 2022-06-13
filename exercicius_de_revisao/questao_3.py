# 3. Escreva um programa em Python que gere e exiba a sequência de números abaixo:
# 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, ...
# ou seja, cada i-ésimo elemento da sequência aparece i vezes repetido na lista. O valor de i
# deve ser informado pelo informado pelo usuário no início da execução do programa

i = 0
for i in range(7):
    for j in range(i):
        print(i)