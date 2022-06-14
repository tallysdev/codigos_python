# 5. Uma matriz quadrada de números inteiros distintos é dita formar um quadrado mágico
# quando a soma dos elementos em qualquer das suas linhas, colunas e diagonais é a
# mesma. A matriz abaixo, por exemplo, é um quadrado mágico de ordem 3, pois a soma dos
# elementos em qualquer linha, coluna ou diagonal é igual a 15. Escreva um programa em
# Python de gere aleatoriamente um quadrado mágico de ordem 3, com valores
# compreendidos entre 1 e 9. Os valores devem ser armazenados em uma matriz, que deve
# ser exiba na tela ao final da execução do programa

        # [
        
        #   1   9   2
        #   3   5   7
        #   8   1   6

        # ]

from random import shuffle 


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
achou = False
while not achou:
  shuffle(lista)
  l1 = lista[0] + lista[1] + lista[2]
  l2 = lista[3] + lista[4] + lista[5]
  l3 = lista[6] + lista[7] + lista[8]
  c1 = lista[0] + lista[3] + lista[6]
  c2 = lista[1] + lista[4] + lista[7]
  c3 = lista[2] + lista[5] + lista[8]
  d1 = lista[0] + lista[4] + lista[8]
  d2 = lista[2] + lista[4] + lista[6]
  if l1 == 15 and l2 == 15 and l3 == 15 and \
     c1 == 15 and c2 == 15 and c3 == 15 and \
     d1 == 15 and d2 == 15:
       achou = True
print()
print("Quadrado Mágico")
for i in range(3):
  print('|', end='')
  for j in range(3):
    print('%3d'%lista[i*3+j], end='')
  print('  |')
  