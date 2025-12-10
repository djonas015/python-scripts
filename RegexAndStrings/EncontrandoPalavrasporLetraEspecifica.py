import re

livro = input("Insira o titulo do livro: ")
padrao_letra = r'\w*'
letra = input("Insira a letra: ")
padraocompleto = rf'\b{letra}{padrao_letra}'
print(re.findall(padraocompleto, livro))
