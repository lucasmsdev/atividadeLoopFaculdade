import random

num = int(input("Digite o número de vezes que deseja jogar a moeda: "))

for i in range(1, num):
    resultado = random.randint(0, 1)
    if resultado == 1:
        print("O resultado é cara")
    elif resultado == 0:
        print("O reultado é coroa")    
