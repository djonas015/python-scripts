lista = ['Ana', 'Pedro', 'Carlos']
new_convidado = input("Insira o nome do novo convidado: ")
posicao = int(input("Insira a posição na lista (iniciando em 0): "))
lista.insert(posicao-1, new_convidado)
print(f"Lista atualizada: {lista}")
