import random
l = []
a = 20
while a != 0:    
    print("(1) Criar lista")
    print("(2) Ler lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Esta ordenada por ordem crescente")
    print("(8) Esta ordenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")
    a = int(input("Escolha uma das seguintes opções: "))
    if a == 1:
        n = int(input("Quantos elementos aleatórios quer gerar? "))
        l = []
        i = 0
        while i < n:
            l.append(random.randint(1, 100))
            i = i +1
        print("Lista gerada com sucesso:", l)
    elif a == 2:
        n = int(input("Quantos elementos vai introduzir? "))
        l = []
        i = 0
        while i < n:
            val = int(input(f"Elemento {i+1}: "))
            l.append(val)
            i += 1
        print("Lista guardada:", l)
    elif a == 3:
        if len(l) == 0:
            print("A lista está vazia.")
        else:
            soma = 0
            i = 0
            while i < len(l):
                soma += l[i]
                i += 1
            print("Soma dos elementos:", soma)
    elif a == 4:
        if len(l) == 0:
            print("A lista está vazia.")
        else:
            soma = 0
            i = 0
            while i < len(l):
                soma += l[i]
                i += 1
            media = soma / len(l)
            print("Média dos elementos:", media)
    elif a == 5:
        if len(l) == 0:
            print("A lista está vazia.")
        else:
            maior = l[0]
            i = 1
            while i < len(l):
                if l[i] > maior:
                    maior = l[i]
                i += 1
            print("Maior elemento:", maior)
    elif a == 6:
        if len(l) == 0:
            print("A lista está vazia.")
        else:
            menor = l[0]
            i = 1
            while i < len(l):
                if l[i] < menor:
                    menor = l[i]
                i += 1
            print("Menor elemento:", menor)
    elif a == 7:
        if len(l) == 0:
            print("A lista está vazia.")
        else:
            crescente = True
            i = 0
            while i < len(l) - 1:
                if l[i] > l[i + 1]:
                    crescente = False
                i += 1
            if crescente:
                print("Sim, está ordenada por ordem crescente.")
            else:
                print("Não está ordenada por ordem crescente.")
    elif a == 8:
        if len(l) == 0:
            print("A lista está vazia.")
        else:
            decrescente = True
            i = 0
            while i < len(l) - 1:
                if l[i] < l[i + 1]:
                    decrescente = False
                i += 1
            if decrescente:
                print("Sim, está ordenada por ordem decrescente.")
            else:
                print("Não está ordenada por ordem decrescente.")
    elif a == 9:
        if len(l) == 0:
            print("A lista está vazia.")
        else:
            elem = int(input("Qual é o elemento que deseja procurar? "))
            pos = -1
            i = 0
            while i < len(l):
                # Guarda a posição apenas se ainda não tiver encontrado (evita break)
                if l[i] == elem and pos == -1:
                    pos = i
                i += 1
            print(f"Resultado da procura (posição): {pos}")
    elif a == 0:
        print("\nA encerrar a aplicação.")
        print("Lista final guardada:", l)
    else:
        print("Opção inválida! Escolha um número entre 0 e 9.")