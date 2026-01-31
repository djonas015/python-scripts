usuarios_db = [{"nome": None, "email": None}]
import os 

def menu():
    while True:
        opcoes_menu()
        escolher_opcoes_menu()


def opcoes_menu():
    print("Selecione uma opção:")
    print("1. Criar usuário")
    print("2. Listar usuários")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Sair")

def escolher_opcoes_menu():
    opcao = input("Digite o número da opção desejada: ")
    if opcao == '1':
        criar_usuario()
    elif opcao == '2':
        listar_usuarios()
    elif opcao == '3':
        atualizar_usuario()
    elif opcao == '4':
        deletar_usuario()
    elif opcao == '5':
        encerrar_programa()


def limpar_tela():
    os.system('cls')


def encerrar_programa():
    limpar_tela()
    print("Programa encerrado.")
    exit()
    

def criar_usuario():
    limpar_tela()
    nome_user = input("Digite o nome do usuário: ")
    email_user = input("Digite o email do usuário: ")
    usuario = {
        "nome": nome_user,
        "email": email_user
    }
    usuarios_db.append(usuario)
    limpar_tela()
    menu()
    


def listar_usuarios():
    for usuario in usuarios_db:
        print(f"Nome: {usuario["nome"]}, Email: {usuario["email"]}")  


def atualizar_usuario():
    pass


def deletar_usuario():
    pass


if __name__ == "__main__":
    menu()