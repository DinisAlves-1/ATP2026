import random
print("Bem-vindo!")
print("Este é o jogo da corrida aos 100.")
print("Na sua vez cada jogador deve escolher um número entre 1 e 10 para somar a um total partilhado que começa em 0.")
print("O primeiro a chegar aos 100 vence!")


reiniciar = "s"
while reiniciar == "s":    
    a = input("Quem vai começar o jogo?  (1-Computador/2-Utilizador)")
    soma=0
    if a == "1":
        nc=1
        soma=1
        print("Eu escolho o número",nc)
        print("A soma total é",soma)
        while soma != 100:
            n=int(input("Digite um número entre 1 e 10 para adicionar à soma:  "))
            while n < 1 or n > 10:
                print("Tem que ser um número entre 1 e 10")
                n = int(input("Digite um número de 1 a 10:  "))
            soma = soma + n
            print("A soma total é",soma)
            nc = 11 - n
            print("Eu escolho o número",nc)
            soma = soma + nc
            print("A soma total é",soma)
        print("Ganhei!")
    elif a == "2":
        while soma != 100:
            n = int(input("Digite um número de 1 a 10:  "))
            while n < 1 or n > 10:
                print("Tem que ser um número entre 1 e 10")
                n = int(input("Digite um número de 1 a 10:  "))

            soma = soma + n
            print(f"A soma total é {soma}")
            if soma == 100:
                print("Parabéns! Ganhaste")
            elif soma % 11 == 1:
                nc = random.randint(1,10)
                print("Eu escolho o número",nc)
                soma = soma + nc
                print(f"A soma total é {soma}")
                if soma == 100:
                    print("Ganhei!")
            elif soma % 11 != 1:
                nc = 11 - (soma-1) % 11
                print("Eu escolho o número",nc)
                soma = soma + nc
                print(f"A soma total é {soma}")
                if soma == 100:
                    print("Ganhei!")
    reiniciar = input("Deseja voltar a jogar? (s-SIM / n-NÃO)   ")   


        
 

    
        


    

