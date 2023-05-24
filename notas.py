#Notas
from marquinhos.MARCUS import capturar_db


True
while True:
    linha = "================================================================================================================"
    create_usuario = input("Criar usuario---> ")
    usuario = input("digite seu usuário---> ")
    senha = int(input("digite sua senha--->"))
    dados = {"Usuarios" : list()}
    if usuario in dados:
        aluno = input("De qual aluno você deseja inserir as notas---> ")
        print(linha)
        querer = input(f"Deseja inserir as notas de {aluno}? sim(1) não(2)---> ")
        if querer == "1":
            nota1 = float(input("Primeira nota---> "))
            nota2 = float(input("Segunda nota---> "))
            nota3 = float(input("Terceira nota---> "))
            nota4 = float(input("Quarta nota---> "))
            media = (nota1 + nota2 + nota3 + nota4)/4
            if media >= 6:
                print(f"o aluno foi aprovado com a média de {media}!")
            elif media < 6:
                print(f"O aluno foi reprovado com a media de {media}")
        
    
        elif querer == "2":
            print("Finalizando Programa...")
            print("Programa Finalizado.")
        else:
            print("Erro, Caracteres inválidas. Tente Novamente")
            False
    else:
        input("Usuario inexistente,")
    
    