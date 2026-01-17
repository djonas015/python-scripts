"""Sistema de Gestão de Alunos

Parecido com: cadastro e listagem de restaurantes

Funcionalidades

Cadastrar aluno (nome, curso, matrícula)

Listar alunos

Ativar/desativar matrícula

Buscar aluno pelo nome ou matrícula

Excluir aluno"""

import os


alunos_cadastrados = [{"nome": "Pedro", "ano": "3°Médio", "ativo": False},
                      {"nome": "Arthur", "ano": "3°Médio", "ativo": True},
                      {"nome": "Igor", "ano": "3°Médio", "ativo": False}]


def nome_do_programa():
    print("""\n❝𝐇𝐚𝐫𝐯𝐚𝐫𝐝 𝐒𝐜𝐡𝐨𝐨𝐥❞\n""")

    
def funcionalidades():
    print("1.Cadastrar Aluno")
    print("2.Listar alunos")
    print("3.Ativar ou Desativar matrícula")
    print("4.Buscar Aluno")
    print("5.Excluir Aluno")
    print("6.Sair\n")
    

def subtitulo_do_sistema(texto):
    os.system('cls')
    print(texto)
    print()


def voltar_ao_menu():
    input("\nInsira uma tecla para voltar ao menu: ")
    main()


def cadastrar_alunos():
    subtitulo_do_sistema("Cadastre Novos Alunos")
    nome_do_aluno = input("Digite o nome do aluno: ")
    ano_letivo_do_aluno = input(f"Digite o ano letivo do {nome_do_aluno}: ")
    dados_do_aluno = {"nome": nome_do_aluno,
                      "ano": ano_letivo_do_aluno,
                      "ativo": False}
    alunos_cadastrados.append(dados_do_aluno)
    print("O aluno foi cadastrado com sucesso.")
    voltar_ao_menu()


def listar_alunos():
    subtitulo_do_sistema("Lista de alunos cadastrados")
    print(f"{"Nome do aluno".ljust(22)} | {"Série".ljust(22)} | Status")
    for aluno in alunos_cadastrados:
        nome_aluno = aluno["nome"]
        serie_aluno = aluno["ano"]
        ativo = "matrícula ativada" if aluno["ativo"] else "matrícula desativada" #ENTENDER O ERRO NO TERMINAL
        print(f"{nome_aluno.ljust(22)} | {serie_aluno.ljust(22)} | {ativo}")
    voltar_ao_menu()


def estado_de_matricula():
    subtitulo_do_sistema("""Ative ou Desative a matrícula do aluno""")
    nome_aluno = input("Insira o nome do aluno que deseja mudar o estado da matrícula: ")
    aluno_encontrado = False
    for aluno in alunos_cadastrados:
        if nome_aluno == aluno["nome"]:
            aluno_encontrado = True
            aluno["ativo"] = not aluno["ativo"]
            mensagem = f"\nO aluno {nome_aluno} está com a matrícula ativada com sucesso" if aluno["ativo"] else f"O aluno {nome_aluno} foi desativado com sucesso"
            print(mensagem)

    if not aluno_encontrado:
        print("\nAluno não encontrado")
    voltar_ao_menu()


def buscar_aluno():
    subtitulo_do_sistema("Busque o aluno no sistema")
    nome_aluno = input("Nome do aluno: ")
    aluno_encontrado = False
    for aluno in alunos_cadastrados:
        if nome_aluno == aluno["nome"]:
            mensagem = f"\nAluno {nome_aluno} encontrado com sucesso!"
            aluno_encontrado = True
            print(mensagem)
            voltar_ao_menu()
    if not aluno_encontrado:
        print("\nAluno não encontrado")
    voltar_ao_menu()


def excluir_aluno():
    subtitulo_do_sistema("Exclua o Aluno do Sistema")
    nome_aluno = input("Insira o nome do aluno que deseja excluir: ")
    for aluno in alunos_cadastrados:
        if nome_aluno == aluno["nome"]:
            alunos_cadastrados.remove(aluno)
            print("Aluno excluido do sistema")
            voltar_ao_menu()
    else:
        print("Aluno não encontrado")
    voltar_ao_menu()


def sair():
    os.system("cls")
    print("Finalizando o Programa...")


def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))
    if opcao_escolhida == 1:
        cadastrar_alunos()
    elif opcao_escolhida == 2:
        listar_alunos()
    elif opcao_escolhida == 3:
        estado_de_matricula()
    elif opcao_escolhida == 4:
        buscar_aluno()
    elif opcao_escolhida == 5:
        excluir_aluno()
    elif opcao_escolhida == 6:
        sair()
    else:
        voltar_ao_menu()


def main():
    os.system('cls')
    nome_do_programa()
    funcionalidades()
    escolher_opcao()


if __name__ == "__main__":
    main()
