# matriz1 = []
# matriz2 = [[1, 2], [3, 4]]
# matriz3 = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
#  ]

# print(matriz1,'\n')
# print(matriz2,'\n')
# print(matriz3,'\n')

print('Programa Matrizes')
print('Informe as dimensões da matriz')
m = int(input('Quantas linhas? '))
n = int(input('Quantas colunas? '))
mat = []
for i in range(m):
    mat.append([])
    for j in range(n):
        v = int(input('M[%d][%d]: '%(i+1,j+1)))
        mat[i].append(v)
print()
print('Matriz lida')
for i in range(m):
    print('|', end='')
    for j in range(n):
        print('%3d'%mat[i][j], end='')
    print(' |')
