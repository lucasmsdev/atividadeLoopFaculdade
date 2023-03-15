dep = float(input("Digite aqui o valor do depósito que deseja fazer: "))
taxa = 0.005
mes = 1
saldo = dep

while mes <= 12:
    saldo = saldo + (saldo * taxa)
    print("O saldo do mês", mes,"é de:", saldo)
    mes = mes + 1