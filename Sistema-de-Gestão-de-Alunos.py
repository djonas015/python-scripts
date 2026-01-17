"""Sistema de Gestão de Alunos

Parecido com: cadastro e listagem de restaurantes

Funcionalidades

Cadastrar aluno (nome, curso, matrícula)

Listar alunos

Ativar/desativar matrícula

Buscar aluno pelo nome ou matrícula

Excluir aluno"""

import os
import sys


alunos_cadastrados = [{"nome": "Pedro", "curso": "Economia", "matrícula": False},
                      {"nome": "Arthur", "curso": "Engenharia", "matrícula": True},
                      {"nome": "Igor", "curso": "Letras", "matrícula": False}]


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
    curso_do_aluno = input(f"Digite o ano letivo do {nome_do_aluno}: ")
    dados_do_aluno = {"nome": nome_do_aluno,
                      "curso": curso_do_aluno,
                      "matrícula": False}
    alunos_cadastrados.append(dados_do_aluno)
    print("O aluno foi cadastrado com sucesso.")
    voltar_ao_menu()


def listar_alunos():
    subtitulo_do_sistema("Lista de alunos cadastrados")
    print(f"{"Nome do aluno".ljust(22)} | {"Curso".ljust(22)} | Status de Matrícula\n")
    for aluno in alunos_cadastrados:
        nome_aluno = aluno["nome"]
        curso_aluno = aluno["curso"]
        ativo = "matrícula ativada" if aluno["matrícula"] else "matrícula desativada"
        print(f"{nome_aluno.ljust(22)} | {curso_aluno.ljust(22)} | {ativo}")
    voltar_ao_menu()


def estado_de_matricula():
    subtitulo_do_sistema("""Ative ou Desative a matrícula do aluno""")
    nome_aluno = input("Insira o nome do aluno que deseja mudar o estado da matrícula: ")
    aluno_encontrado = False
    for aluno in alunos_cadastrados:
        if nome_aluno == aluno["nome"]:
            aluno_encontrado = True
            aluno["matrícula"] = not aluno["matrícula"]
            mensagem = f"\nO aluno {nome_aluno} está com a matrícula ativada com sucesso" if aluno["matrícula"] else f"O aluno {nome_aluno} foi desativado com sucesso"
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
    sys.exit()


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
        print("Opção inválida")
        voltar_ao_menu()


def main():
    os.system('cls')
    nome_do_programa()
    funcionalidades()
    escolher_opcao()


if __name__ == "__main__":
    main()
