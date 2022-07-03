#questão 15
#An=6A(n-1)-8A(n-2) a0=1 a1=0

recursao=int(input("Digite um recursao:"))

def recurcaoQ15(recursao):
  if recursao==0:
    return 1
  elif recursao==1:
    return 0
  else:
    return 6*recurcaoQ15(recursao-1)-8*recurcaoQ15(recursao-2)

print('Usano a Recursão:',recurcaoQ15(recursao))

a0=1
a1=0
an=1
if recursao==1:
  an=0
else:
  for i in range(2,recursao+1):
    an=6*a1-8*a0
    a0=a1
    a1=an

print('Por Loop:',an)

def solucao(n):
  return (-1)*(4**n)+2*(2**n)

print('Por Soluçaõ:', solucao(recursao))