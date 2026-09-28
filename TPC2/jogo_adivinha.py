import random
print("Bem vindo ao jogo da adivinha!")
reiniciar = "s"
while reiniciar == "s":
    a = input("Quem vai adivinhar o número? (1-utilizador / 2-computador)  ")
    while a != "1" and a != "2":
        print("Tem que inserir o número 1 ou o número 2.")
        a = input("Quem vai adivinhar o número? (1-utilizador / 2-computador)  ")

    if a == "1":
        ns = random.randint(0,100)         #ns é o número escolhido pelo computador e o n pelo utilizador até o mesmo acretar
        n = int(input("Adivinha o número de 0 a 100:  "))         
        while n < 0 or n > 100:
            print("Tem que ser um número entre 0 e 100")
            n = int(input("Adivinha o número de 0 a 100:  "))

        tentativas = 1
        while n != ns:
            if n < ns:
                print("O número que pensei é maior que", n )
            else:
                print("O número que pensei é menor que", n)
            tentativas = tentativas + 1
            n = int(input("Adivinha o número de 0 a 100:  "))
            while n < 0 or n > 100:
                print("Tem que ser um número entre 0 e 100")
                n = int(input("Adivinha o número de 0 a 100:  "))
        

        print ("Acertou! O número é", ns ,". Precisaste de", tentativas ,"tentativas.")
    elif a == "2":  
        max = 100
        min = 0
        print("Pensa em um número de 0 a 100.")
        enter = input("Pressiona a tecla 'Enter' para continuar.")
        while enter != "":
            enter = input("Pressiona a tecla 'Enter' para continuar.") 
        n = 50
        r = input(f"O número é {n}?  (1-maior / 2-menor / 3-certo)  ")
        while r != "1" and r != "2" and r != "3":
            print("Tem que inserir o número 1 , 2 ou 3")
            r = input(f"O número é {n}?  (1-maior / 2-menor / 3-certo)  ")
        tentativas = 1
        while r == "1" or r == "2":
            if r == "1":
                min = n + 1
                n = (max + min)//2
                tentativas = tentativas + 1
                r = input(f"O número é {n} ?  (1-maior / 2-menor / 3-certo)  ") 
                while r != "1" and r != "2" and r != "3":
                    print("Tem que inserir o número 1 , 2 ou 3")
                    r = input(f"O número é {n}?  (1-maior / 2-menor / 3-certo)  ")   
            elif r == "2":
                max = n - 1 
                n = (max + min)//2
                tentativas = tentativas + 1
                r = input(f"O número é {n} ?  (1-maior / 2-menor / 3-certo)  ")
                while r != "1" and r != "2" and r != "3":
                    print("Tem que inserir o número 1 , 2 ou 3")
                    r = input(f"O número é {n}?  (1-maior / 2-menor / 3-certo)  ")
    
        print("O número era",n,". Precisei de",tentativas,"tentativas.")
    reiniciar = input("Deseja voltar a jogar? (s-SIM / n-NÃO)   ")







    



