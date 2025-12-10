voluntario = []
while True:
    nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
    if nome == 'sair':
        break
    else:
        voluntario.append(nome)
        print(voluntario)
