import sys

while True:
    print("\f1 == Adição (+)\f"
          "2 == Subtração (-)\f"
          "3 == Multiplicação (*)\f"
          "4 == Divisão (\)\f"
          "5 == SAIR\f")
    operador = int(input("\fSelecione um número: "))
    match operador:
        case 1:
            adicao1 = float(input("Insira o primeiro numero: "))
            adicao2 = float(input(f"{adicao1} + ___ = ___" 
                                  "\fInsira o segundo número: "))
            somatoria = adicao1 + adicao2
            print(f"{adicao1} + {adicao2} = {somatoria}")
        case 2:
            subtracao1 = float(input("Insira o primeiro número: "))
            subtracao2 = float(input(f"{subtracao1} - ___ = ___" 
                                     "\fInsira o segundo numero: "))
            sub = subtracao1 - subtracao2
            print(f"{subtracao1} - {subtracao2} = {sub}")
        case 3:
            multiplicao1 = float(input("Insira o primeiro número: "))
            multiplicao2 = float(input(f"{multiplicao1} x ___ = ___" 
                                       "\fInsira o segundo numero: "))
            multi = multiplicao1 * multiplicao2
            print(f"{multiplicao1} x {multiplicao2} = {multi}")
        case 4:
            divisao1 = float(input("Insira o primeiro número: "))
            divisao2 = float(input(f"{divisao1} / ___ = ___" 
                                   "\fInsira o segundo numero: "))
            if divisao2 == 0:
                print("ERRO! Divisão por 0.")
            else:
                div = divisao1 / divisao2
                print(f"{divisao1} / {divisao2} = {div}")
        case 5:
            print("Encerrando as operações!")
            sys.exit()
        case _:
            print("Opção inválida!")
