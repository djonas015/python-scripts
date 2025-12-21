numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
operador = input("Selecione a operação (| + | - | * | / |): ")
operacoes = {
    "+": lambda n1, n2: n1 + n2,
    "-": lambda n1, n2: n1 - n2,
    "*": lambda n1, n2: n1 * n2,
    "/": lambda n1, n2: n1 / n2
}
resultado = operacoes[operador](numero_1, numero_2)

print(f"Resultado: {resultado}")
