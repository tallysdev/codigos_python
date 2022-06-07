from random import randint


tabu = [
 ['_', '_', '_'],
 ['_', '_', '_'],
 ['_', '_', '_'],
 [' ', ' ', ' '],
 ['^', '^', '^'],
 ['1', '2', '3'],
 ['4', '5', '6'],
 ['7', '8', '9']
 ]
print("Tabuleiro")
for i in range(8):
    for j in range(3):
        print(tabu[i][j], end=' ')
 
    print()
print()

tabu = [
 ['_', '_', '_'],
 ['_', '_', '_'],
 ['_', '_', '_']
 ]
print("Tabuleiro oficial")
for i in range(3):
    for j in range(3):
        print(tabu[i][j], end=' ')
 
    print()
print()

ganhou = False
jogadas = 0
while jogadas < 9 and not(ganhou):

    jog = int(input("Informe a posição da sua jogada:\t"))
    i = (jog-1) // 3
    j = (jog-1) % 3
    tabu[i][j] = 'O'
    jogadas+=1
    print("Tabuleiro oficial")
    for i in range(3):
        for j in range(3):
            print(tabu[i][j], end=' ')
 
        print()
    print()

    print('Jogada do computador')
    achou = False
    while not achou:
        jcomp = randint(0,8)
        i = (jcomp) // 3
        j = (jcomp) % 3
        if tabu[i][j]=='_':
            tabu[i][j] = 'X'
            achou = True
            jogadas+=1

    
    print("Tabuleiro oficial")
    for i in range(3):
        for j in range(3):
            print(tabu[i][j], end=' ')
 
        print()
    print()


    if (tabu[0][0] == tabu[0][1]) and (tabu[0][1] == tabu[0][2]) and (tabu[0][2] != '_'):
        vit = tabu[0][0]
        ganhou = True
    elif (tabu[1][0] == tabu[1][1]) and (tabu[1][1] == tabu[1][2]) and (tabu[1][2] != '_'):
        vit = tabu[1][0]
        ganhou = True
    elif (tabu[2][0] == tabu[2][1]) and (tabu[2][1] == tabu[2][2]) and (tabu[2][2] != '_'):
        vit = tabu[2][0]
        ganhou = True
    elif (tabu[0][0] == tabu[1][0]) and (tabu[1][0] == tabu[2][0]) and (tabu[2][0] != '_'):
        vit = tabu[0][0]
        ganhou = True
    elif (tabu[0][1] == tabu[1][1]) and (tabu[1][1] == tabu[2][1]) and (tabu[2][1] != '_'):
        vit = tabu[0][1]
        ganhou = True
    elif (tabu[0][2] == tabu[1][2]) and (tabu[1][2] == tabu[2][2]) and (tabu[2][2] != '_'):
        vit = tabu[0][0]
        ganhou = True
    elif (tabu[0][0] == tabu[1][1]) and (tabu[1][1] == tabu[2][2]) and (tabu[2][2] != '_'):
        vit = tabu[0][0]
        ganhou = True
    elif (tabu[0][2] == tabu[1][1]) and (tabu[1][1] == tabu[2][0]) and (tabu[2][0] != '_'):
        vit = tabu[0][2]
        ganhou = True

if jogadas == 8:
    print('Empateeee')

print('Quem ganhou foi o (',vit,')')

