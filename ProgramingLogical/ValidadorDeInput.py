def menu():
    print("\nBem vindo à Indian-Airlines\n")
    print("Selecione o seu destino de preferência")
    print("1. BRASIL")
    print("2. ARGENTINA")
    print("3. URUGUAI\n")


def main():
    menu()
    entrada = int(input("Insira um número: "))
    menu_opcoes(entrada)


def menu_opcoes(entrada):
    continuar = True
    while continuar:
        try:
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
        except ValueError:
            print("Opção inválida, Você deve digitar um número")


if __name__ == "__main__":
    main()
