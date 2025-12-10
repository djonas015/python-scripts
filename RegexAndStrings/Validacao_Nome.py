import re

nome = input("Insira o nome: ")
if re.fullmatch(r'[a-z]+', nome):
    print("nome valido!")
else:
    print("não é valido.")
