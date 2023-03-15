num = int(input("Digite um número para achar seu fatorial: "))
fat = 1
i = 2
    
while i <= num:
    fat = fat*i
    i = i + 1

print("O valor de %d! é: " %num, fat)