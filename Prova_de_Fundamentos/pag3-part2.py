from math import sqrt
#questão 22
#Ln=L(n-1)+L(n-2) L1=1 L2=3 n>=3

recursaoq22=int(input("Digite um recursaoq22:"))

def funcao(recursaoq22):
  if recursaoq22==1:
    return 1
  elif recursaoq22==2:
    return 3
  else:
    return funcao(recursaoq22-1) + funcao(recursaoq22-2)

print(funcao(recursaoq22))

a1=1
a0=3
resultado=1
if recursaoq22==2:
  resultado=a0
else:
  for i in range(3,recursaoq22+1):
      resultado=a1+a0
      a1=a0
      a0=resultado

print(resultado)

def recursao(n):
  return (((1+sqrt(5))/2)**n)+(((1-sqrt(5))/2)**n)

print("%.2f"%recursao(recursaoq22))