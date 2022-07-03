from math import sqrt
#questão 22
#Ln=L(n-1)+L(n-2) L1=1 L2=3 n>=3

recursao22=int(input("Digite um valor:"))

def recursaoQ22(recursao22):
  if recursao22==1:
    return 1
  elif recursao22==2:
    return 3
  else:
    return recursaoQ22(recursao22-1) + recursaoQ22(recursao22-2)

print('Usando a Recursão:',recursaoQ22(recursao22))

a1_22=1
a0_22=3
resultado_22=1
if recursao22==2:
  resultado_22=a0_22
else:
  for i in range(3,recursao22+1):
      resultado=a1_22+a0_22
      a1_22=a0_22
      a0_22=resultado_22

print('Por loop:',resultado_22)

def recursao(n):
  return (((1+sqrt(5))/2)**n)+(((1-sqrt(5))/2)**n)

print('Por Solução:',"%.2f"%recursao(recursao22))