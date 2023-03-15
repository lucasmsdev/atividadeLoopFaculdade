num = int(input("Digite um número de 1 a 10: "))

if num > 10:
    print("Digite um valor válido de 1 a 10")
    exit()
else:
    print("Tábuada do", num)
    for i in range(10):
        print("%d x %d = %d" % (num, i+1, num*(i+1)))
        

