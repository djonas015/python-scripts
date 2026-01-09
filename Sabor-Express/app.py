import os

restaurantes = [{"nome": "Pizza", "categoria": "Italiana", "ativo": False},
                {"nome": "Sushi", "categoria": "Japonesa", "ativo": True},
                {"nome": "Cantina", "categoria": "Brasileira", "ativo": False}]


def exibir_nome_do_programa():
    print("""
    ▒█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▒█▀▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
    ░▀▀▀▄▄ █▄▄█ █▀▀▄ █░░█ █▄▄▀ 　 ▒█▀▀▀ ▄▀▄ █░░█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
    ▒█▄▄▄█ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▒█▄▄▄ ▀░▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀\n""")


def exibir_opcoes():
    """Essa função apenas exibe na tela as opções do programa"""
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")


def finalizar_app():
    """Essa função é responsável pelo texto de finalizar o app"""
    exibir_subtitulo("Finalizando o app")


def voltar_ao_menu_principal():
    """Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal"""
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()


def opcao_invalida():
    """Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal"""
    print("Oção inválida!\n")
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    """Essa função é responsável por limpar a tela do terminal e por ser o esqueleto após o user passar da primeira tela do programa 
    
    Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo"""
    os.system("cls")
    linha = "*" * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """Essa função é responsável por cadastrar novos restaurantes
    
    input
    -nome do restaurante para cadastro
    -categoria desse mesmo restaurante
    
    output
    -adiciona esses dados na lista de restaurantes
    
    """
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Insira o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante,
                            "categoria": categoria,
                            "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"O Restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()


def listar_restaurantes():
    """Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela"""
    exibir_subtitulo("Listando os restaurantes")
    print(f"{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(22)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f".{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}")
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """Essa função é responsável por alternar o estado do restaurante
    
    input
    -user insere o nome do restaurante que deseja alternar o estado(ativo/desativado)
    
    """
    exibir_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input("Insira o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
            
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    voltar_ao_menu_principal()


def escolher_opcao():
    """Essa função é responsável por fazer o user escolher a opção no programa
    
    input
    -user escolhe as opções do programa de 1 a 4
    
    """
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    """Essa função é responsável por limpar a tela, exibir o nome do programa e opções
    Função principal que inicia o programa """
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()