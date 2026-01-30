dados_usuario = [{"nome": {},
                  "idade": {},
                  "salario": {}}]


def informacoes_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    if idade < 17:
        print("Você não pode realizar essa operação")
    else:
        salario = float(input("Digite seu sálario: "))
        if salario < 0:
            print("Você não pode realizar essa operação")
        else:
            print(f"Olá {nome}, você possui {idade} e possui um sálario de R${salario}")
            dados = {"nome": {nome},
                     "idade": {idade},
                     "salario": {salario}}
            dados_usuario.append(dados)


def salvando_dados():
    with open("dados_user.txt", "x", "utf-8") as arquivo:
        arquivo.writelines(dados_usuario) #Resolvendo esse bug do writelines e afins


def main():
    informacoes_usuario()
    salvando_dados()


if __name__ == "__main__":
    main()
