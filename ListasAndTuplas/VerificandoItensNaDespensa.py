itens = ["Arroz", "Feijão", "Macarrão", "Carne"]


produto = input("Insira o iten que deseja verificar: ")
if produto in itens:
    print(f"{produto} Já está na despensa")
else:
    print(f"{produto} Precisa ser comprado")
print(itens)
