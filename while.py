from random import randint 

rolagem = True
x = 0

while rolagem == True:
        resultado = randint(1, 20)
        if resultado == 20:
            print("você tirou 20!")
            print(f"você levou {x} tentativas para tirar 20")
            rolagem = False
        else:
            x += 1
      



    
    
    
    
    
   

        
