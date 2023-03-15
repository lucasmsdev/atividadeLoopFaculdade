#constantes
votosJ = 0
votosC = 0
votosN = 0
votosNl = 0
votosB = 0

#"menu"
print("As opções são:\n1- Candidato Jair Rodriguez\n2- Candidato Carlos Luz\n3- Candidato Neves Rochas\n4- Nulo\n5- Branco")

#Laço de repetição
while True: 

    
    voto = int(input("Escolha uma das opções acima para votar: "))
    if voto == 1 or voto == 2 or voto == 3 or voto ==4 or voto == 5:
        #contagem de votos
        if voto == 1:
            votosJ += 1


        elif voto == 2:
            votosC += 1
        

        elif voto == 3:
            votosN += 1


        elif voto == 4:
            votosNl += 1


        elif voto == 5:  
            votosB += 1

     #Contagem de votos e exibição dos resultados.       
    else:
        votosTotais = votosJ + votosC + votosN + votosNl + votosB

        porVotosNl = votosNl/votosTotais * 100
        porVotosB = votosB/votosTotais * 100

        if votosJ > votosC and votosJ > votosN:
            print("O candidato Jair Rodriguez foi eleito com:", votosJ)
            print("O candidato Carlos Luz teve", votosC,"votos")
            print("O candidato Neves Rocha teve", votosN,"votos\nA porcentagem de votos nulos foi de:",porVotosNl,"\nA porcentagem de votos nulos foi de:", porVotosB)
            exit(0)
            

        elif votosC > votosN and votosC > votosJ:
            print("O candidato Carlos Luz foi eleito com:", votosC)
            print("O candidato Jair Rodriguez teve", votosJ,"votos")
            print("O candidato Neves Rocha teve", votosN,"votos\nA porcentagem de votos nulos foi de:",porVotosNl,"\nA porcentagem de votos nulos foi de:", porVotosB)
            exit(0)

        elif votosN > votosC and votosN > votosJ:
            print("O candidato Neves Rocha foi eleito com:", votosN)
            print("O candidato Jair Rodriguez teve", votosJ,"votos")
            print("O candidato Carlos Luz teve", votosC,"votos\nA porcentagem de votos nulos foi de:",porVotosNl,"\nA porcentagem de votos nulos foi de:", porVotosB)  
            exit(0)  

        elif votosN == votosC or votosC == votosJ or votosN == votosJ:
            print("Dois canditos tiveram a mesma quantidade de votos, é necessário um segundo turno.")    
            exit(0)


                    