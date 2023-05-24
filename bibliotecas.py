from random import randint

pergunta = input("você lembra da sua velocidade?---> ")

if pergunta == "sim":
    velocidade = int(input("sua velocidade---> "))

elif pergunta == "não":
    velocidade = randint(1, 120)
    print(f"você estava a {velocidade}km/h")

if velocidade <= 90 and velocidade >= 30:
    print("pode passar")

elif velocidade <= 30:
    print("voce está muito lento, favor mudar de mão")

elif velocidade >= 90:
   multa = velocidade - 90
   print(f"você está excedendo os limites de velocidade a {velocidade}km/h")
   print(f"voce está sendo multado em {multa * 7}R$")
   
else:
    print("Não compreendo")