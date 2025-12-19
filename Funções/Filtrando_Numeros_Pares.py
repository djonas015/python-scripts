numeros = input("Digite os números: ").split()
lista_num = [int(num) for num in numeros]
pares = list(filter(lambda pares: pares % 2 == 0, lista_num))
print(f"Números pares {pares}")
