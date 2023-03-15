maior_num = int(input("Entre com um número: "))


number = int(input("Entre com um número ou digite -1 para parar: "))



while number != -1:
    
        
        soma = maior_num + number
        
        number = int(input("Entre com um número ou digite -1 para parar: "))
        maior_num = soma
    
print("A soma dos números é: ", soma)    
