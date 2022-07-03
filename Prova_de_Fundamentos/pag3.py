#questão 15
#An=6A(n-1)-8A(n-2) a0=1 a1=0

recursao15=int(input("informe o valor de n para todas a questões:"))

def recursaoQ15(recursao15):
  if recursao15==0:
    return 1
  elif recursao15==1:
    return 0
  else:
    return 6*recursaoQ15(recursao15-1)-8*recursaoQ15(recursao15-2)

print('Questão 15:\n')
print('Usano a Recursão:',recursaoQ15(recursao15))

a0=1
a1=0
an=1
if recursao15==1:
  an=0
else:
  for i in range(2,recursao15+1):
    an=6*a1-8*a0
    a0=a1
    a1=an

print('Por Loop:',an)

def solucao(n):
  return (-1)*(4**n)+2*(2**n)

print('Por Soluçaõ:', solucao(recursao15))

#############################################################

#questão 16
#An=2A(n-1)+8A(n-2) a0=4 a1=10

recursao16 = recursao15



def recursaoQ16(recursao16):
  if recursao16==0:
    return 4
  elif recursao16==1:
    return 10
  else:
    return 2*recursaoQ16(recursao16-1)+8*recursaoQ16(recursao16-2)

print('\nQuestão 16:\n')
print('Usando a Recursão:',recursaoQ16(recursao16))

valor0=4
valor1=10
resultado=4
if recursao16==1:
  resultado=10
else:
  for i in range(2,recursao16+1):
    resultado=2*valor1+8*valor0
    valor0=valor1
    valor1=resultado

print('Por loop:',resultado)

def solucao(n):
  return 3*(4**n)+(-2)**n

print('Por Solução:', solucao(recursao16))

#######################################################################