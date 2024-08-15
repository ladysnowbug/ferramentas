def exibir_senhas():
    with open("worstpasswords-top30.txt", "r") as arquivo:
        senhas = arquivo.readlines()
        print(senhas) 
        for i in range(min(10, len(senhas))):
           print(senhas[i])

exibir_senhas()

   