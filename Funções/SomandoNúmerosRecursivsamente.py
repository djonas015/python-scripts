def soma_recursiva(n):
    
    if n == 0:
        return 0
    return n + soma_recursiva(n - 1)


num = int(input("Insira o número: "))
resultado = soma_recursiva(num)
print(f"A soma de 1 a {num} é: {resultado}")
