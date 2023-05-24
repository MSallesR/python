import random
jogo = True

energia = random.randint(1, 15)
print("bem vindo ao RPG! Feito por Miguel")
classe = input("Qual sua classe, Guerreiro (1) ou Mago (2)---> ")
if classe == "1":
    print(f"você é um guerreiro das  terras do Norte, você possui 20 de vida e {energia} de estamina!")
    input("gostaria de seguir para a história---> ")
elif classe == "2":
    print(f"você é um mago dos lagos do leste, você possui 20 de vida e {energia} de mana!")
historia1 = input("você está andando pelo seu vilarejo com sua amiga Aurora quando você se depara com uma senhora anâ desesperada, você pergunta: Oque houve? A senhora responde: Meu filho foi raptado por um org das montanhas geladas, por favor me ajude! Você ajuda a recuperar o filho dela, SIM ou NÃO---> ")
if historia1 == "sim" and "SIM":
    while jogo == True:
        print("você parte para a caverna onde a anâ disse ter perdido o filho dela e ao chegar você ouve o rugido: ARRRRRRRRRRRRRRRRRRRRGHHHHHHHHH")
        historia2 = input("você e Aurora se esgueiram para dentro da caverna e precisa decidir se vão atacar o montro de surpresa (1) ou vão desafia-lo (2)---> ")
        if historia2 == "1":
            print("vocês se esgueiram pelos fundos da caverna e tem a possibilidade de um ataque surpresa")
            ataque1 = random.randint(0, 5)
            print(f"você deu {ataque1} de dano nele")
            print("o monstro se vira e reage rapido")
escolha_m = random.randint(1,2)


            


