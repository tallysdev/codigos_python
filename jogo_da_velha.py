velha = [
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
        print(velha[i][j], end=' ')
 
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

    if (velha[0][0] == velha[0][1]) and (velha[0][1] == velha[0][2]) and (velha[0][2] != '_'):
        ganhou = True
    elif (velha[1][0] == velha[1][1]) and (velha[1][1] == velha[1][2]) and (velha[1][2] != '_'):
        ganhou = True
    elif (velha[2][0] == velha[2][1]) and (velha[2][1] == velha[2][2]) and (velha[2][2] != '_'):
        ganhou = True
    elif (velha[0][0] == velha[1][0]) and (velha[1][0] == velha[2][0]) and (velha[2][0] != '_'):
        ganhou = True
    elif (velha[0][1] == velha[1][1]) and (velha[1][1] == velha[2][1]) and (velha[2][1] != '_'):
        ganhou = True
    elif (velha[0][2] == velha[1][2]) and (velha[1][2] == velha[2][2]) and (velha[2][2] != '_'):
        ganhou = True
    elif (velha[0][0] == velha[1][1]) and (velha[1][1] == velha[2][2]) and (velha[2][2] != '_'):
        ganhou = True
    elif (velha[0][2] == velha[1][1]) and (velha[1][1] == velha[2][0]) and (velha[2][0] != '_'):
        ganhou = True



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