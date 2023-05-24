from random import choice



aleatorio = "udhwuyidhdwyukdwigdwhjabdhwjagdywuaj"
escolha = int(input("Quantas letras você quer que a palavra tenha---> "))
palavra = ""
while True:
    if len(palavra) == escolha:
        print("parabens, você acertou!")
        continue

    else:
        palavra += choice(aleatorio)
        print("você errou!")



    
     
    