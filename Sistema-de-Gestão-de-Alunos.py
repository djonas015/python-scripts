"""Sistema de Gestão de Alunos

Parecido com: cadastro e listagem de restaurantes

Funcionalidades

Cadastrar aluno (nome, curso, matrícula)

Listar alunos

Ativar/desativar matrícula

Buscar aluno pelo nome ou matrícula

Excluir aluno"""

import os


alunos_cadastrados = [{"nome": "Pedro", "ano letivo": "3°Médio", "ativo": False},
                      {"nome": "Arthur", "ano letivo": "3°Médio", "ativo": True},
                      {"nome": "Igor", "ano letivo": "3°Médio", "ativo": False}]


def nome_do_programa():
    print("""\n❝𝐇𝐚𝐫𝐯𝐚𝐫𝐝 𝐒𝐜𝐡𝐨𝐨𝐥❞\n""")

    
def funcionalidades():
    print("1.Cadastrar Aluno")
    print("2.Listar alunos")
    print("3.Ativar ou Desativar matrícula")
    print("4.Buscar Aluno")
    print("5.Sair\n")
    

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
    for aluno in alunos_cadastrados:
        nome_aluno = aluno["nome"]
        serie_aluno = aluno["ano letivo"]
        ativo = "matrícula ativada" if aluno["ativo" == True] else "matrícula desativada" #PAREI AQUI, PROXIMO PASSO VALIDAR A FUNÇÃO estado_de_matricula()
        print(f"{nome_aluno.ljust(30)} | {serie_aluno.ljust(30)} | {ativo}")


def estado_de_matricula():


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
        sair()
    else:
        opcao_invalida





def main():
    os.system('cls')
    nome_do_programa()
    funcionalidades()
    escolher_opcao()


if __name__ == "__main__":
    main()
