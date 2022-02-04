import random
n=random.randint(1,10)
x=int(input("Escolha um número entre 1 e 10:"))
contAcertou = 10
contErrou = 10

while(acertou!=3 or errou!=3):
    if (x==n):
        contAcertou += 1
        print("Você acertou !")
        if(contAcertou<3):
             x=int(input("Escolha outro número entre 1 e 10:")
    else:
       contErrou += 1
       print("Você errou !")
       if(contErrou<3):
           x=int(input("Escolha outro número entre 1 e 10:")
            
