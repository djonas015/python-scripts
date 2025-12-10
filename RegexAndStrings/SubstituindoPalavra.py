import re

frase_user = input("Insira a frase")
palavra_antiga = input("Digite a palavra a ser substituida: ")
palavra_nova = input("Palavra nova: ")
substituir = re.sub(rf'\b{palavra_antiga}\b', palavra_nova, frase_user)
print(substituir)
