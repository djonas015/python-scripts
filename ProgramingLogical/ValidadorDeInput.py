continuar = True



print("\nBem vindo à Indian-Airlines\n")
print("Selecione o seu destino de preferência")
print("1. BRASIL")
print("2. ARGENTINA")
print("3. URUGUAI\n")
while continuar:
    try:
        entrada = int(input("\nInsira o número das opções: "))
        if entrada == 1:
            print("Analise as condições da sua passagem para o Brasil")
            continuar = False
        elif entrada == 2:
            print("Analise as condições da sua passagem para o Argentina")
            continuar = False
        elif entrada == 3:
            print("Analise as condições da sua passagem para o Uruguai")
            continuar = False
        else:
            print("Número inválido")
    except:
        print("Opção inválida, tente novamente")
