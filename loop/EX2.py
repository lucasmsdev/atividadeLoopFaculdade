import random

num_secreto = random.randint(0, 100)
tentativa = 1

while tentativa <= 10:
    palpite = int(input("Adivinhe o número secreto: "))
    if palpite == num_secreto:
        print("Você acertou o número!")
        break
    else:
        if palpite > num_secreto:
            print("O número secreto é menor do que ", palpite)
        else:
            print("O número secreto é maior do que", palpite)
    tentativa += 1
    if tentativa > 10:
        print("Suas tentivas acabaram o número era: ", num_secreto)
        