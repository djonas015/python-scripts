lista = set()
while True:
    convidados = input("Insira o nome dos convidados: ")
    if convidados == 'sair':
        break
    else:
        lista.add(convidados)
print(f"Convidados confirmados: {lista}")
