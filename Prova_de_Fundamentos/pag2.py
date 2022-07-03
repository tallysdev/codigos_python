#o primeiro dia de um ano novo, Joseph deposita US $ 1.000 em uma conta que paga 6% de juros compostos mensalmente.  No início de cada mês, ele adiciona $ 200 à sua conta.  Se ele continuar fazendo isso pelos próximos quatro anos (de modo que ele faça 47 depósitos adicionais de $ 200), quanto valerá sua conta exatamente quatro anos depois de abri-la?

#A0=1000
#An+1=200+An*(1,06)
#An=200+(A(n-1))*(1,06)

an=1000
mes=47

for i in range(1,mes+1):
  an= 200+an*1.06

print("Por Loop: %.2f "%an)



def recursao(z):
  if z==0:
    return 1000
  else:
    return 200+ recursao(z-1) * (1.06)
print("Usado a Recursão %.2f"%recursao(mes))
print()
