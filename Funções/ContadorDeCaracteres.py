def contador_de_caracteres(palavra):
    caracteres = len(palavra)
    return f"A palavra possui {caracteres} caracteres"


word = input("Insira a palavra: ")
resultado = contador_de_caracteres(word)
print(resultado)
