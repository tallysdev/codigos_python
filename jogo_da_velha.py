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
while jogada < 10 and not(ganhou):

    jog = int(input("Informe a posição da sua jogada"))
    i = (jog-1) // 3
    j = (jog-1) % 3
    tabu[i][j] = 'O'

    print("Tabuleiro oficial")
    for i in range(3):
        for j in range(3):
            print(tabu[i][j], end=' ')
 
        print()
    print()

    if (tabu[0][0] == tabu[0][1]) and (tabu[0][1] == tabu[0][2]) and (tabu[0][2] != '_'):
        ganhou = True
    elif (tabu[1][0] == tabu[1][1]) and (tabu[1][1] == tabu[1][2]) and (tabu[1][2] != '_'):
        ganhou = True
    elif (tabu[2][0] == tabu[2][1]) and (tabu[2][1] == tabu[2][2]) and (tabu[2][2] != '_'):
        ganhou = True
    elif (tabu[0][0] == tabu[1][0]) and (tabu[1][0] == tabu[2][0]) and (tabu[2][0] != '_'):
        ganhou = True
    elif (tabu[0][1] == tabu[1][1]) and (tabu[1][1] == tabu[2][1]) and (tabu[2][1] != '_'):
        ganhou = True
    elif (tabu[0][2] == tabu[1][2]) and (tabu[1][2] == tabu[2][2]) and (tabu[2][2] != '_'):
        ganhou = True
    elif (tabu[0][0] == tabu[1][1]) and (tabu[1][1] == tabu[2][2]) and (tabu[2][2] != '_'):
        ganhou = True
    elif (tabu[0][2] == tabu[1][1]) and (tabu[1][1] == tabu[2][0]) and (tabu[2][0] != '_'):
        ganhou = True



