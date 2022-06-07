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
jog = int(input('onde voce quer jogar?'))