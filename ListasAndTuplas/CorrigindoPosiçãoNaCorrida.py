Lista = ['Ana', 'João', 'Pedro']
wrong_name = input("Insira o nome incorreto: ")
right_nome = input("Nome correto: ")
if wrong_name in Lista:
    indice = Lista.index(wrong_name)
    Lista[indice] = right_nome
else:
    print("Esse nome não está na lista.")
print(Lista)
