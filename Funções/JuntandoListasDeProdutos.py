fruta = input("Digite as frutas: ").split(", ")
preco = input("Insira o valor dos produtos ").split(", ")
for frutas, precos in zip(fruta, preco):
    print(f"{frutas}: {precos}")

