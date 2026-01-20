"""Projeto clássico e muito útil
Funcionalidades

1Criar tarefa

2Listar tarefas

3Marcar como concluída

4Alterar prioridade

5Excluir tarefa

Campos

Título

Descrição

Prioridade (Alta, Média, Baixa)

Status (pendente/concluída)"""

import os

tarefas = [{"nome": "Beber Água", "prioridade": "Alta", "status": False},
           {"nome": "correr", "prioridade": "Alta", "status": False}]


def nome_programa():
    print("TO DO LIST")


def tela_inicial():
    print("""1. Criar tarefa
             2. Listar tarefas
             3. Alternar Status
             4. Alterar prioridade
             5. Excluir Tarefa""")


def voltar_menu():
    input("Insira uma tecla para voltar ao menu: ")
    main()


def criar_tarefa():
    os.system("cls")
    nome_tarefa = input("Insira a Tarefa: ")
    prioridade_tarefa = input(f"Insira a prioridade de {nome_tarefa}/ Alta, Média, Baixa:  ")
    dados_tarefa = {"nome": nome_tarefa,
                    "prioridade": prioridade_tarefa,
                    "status": False}
    tarefas.append(dados_tarefa)
    print("Tarefa marcada com sucesso")
    voltar_menu()


def listar_tarefas():
    os.system("cls")
    print("Lista de tarefas: ")
    for tarefa in tarefas:
        nome_tarefa = tarefa["nome"]
        prioridade_tarefa = tarefa["prioridade"]
        status_tarefa = "concluida" if tarefa["status"] else "pendente"
        print(f"{nome_tarefa.ljust(20)} | {prioridade_tarefa.ljust(20)} | {status_tarefa}")
    voltar_menu()


def status_tarefa():
    os.system("cls")
    print("Altere o status da tarefa")
    alterando_status = input("Insira o nome da tarefa que deseja alterar o Status: ")
    tarefa_encontrada = False
    for tarefa in tarefas:
        if alterando_status == tarefa["nome"]:
            tarefa_encontrada = True
            tarefa["status"] = not tarefa["status"]
            mensagem = f"O status da {alterando_status} foi alternada com sucesso"
            print(mensagem)
            voltar_menu()

    if not tarefa_encontrada:
        print("Tarefa não encontrada")
        voltar_menu()


def alternar_prioridade():
    os.system("cls")
    print("Alterne a prioridade da tarefa")
    nome_tarefa = input("Insira o nome da tarefa: ")
    tarefa_encontrada = False
    for tarefa in tarefas:
        if nome_tarefa == tarefa["nome"]:
            tarefa_encontrada = True
            prioridade = tarefa["prioridade"]
            print(f"Atualmente a '{nome_tarefa}' tem a prioridade '{prioridade}'")
            alterando_prioridade = input(f"Insira a nova prioridade da tarefa '{nome_tarefa}'")
            tarefa["prioridade"] = alterando_prioridade
            print("Operação realizada com sucesso")
            voltar_menu()
    
    if not tarefa_encontrada:
        print("Tarefa não encontrada")
        voltar_menu()


def excluir_tarefa():
    os.system("cls")
    print("Exclua alguma tarefa da lista")
    nome_tarefa = input("Insira o nome da tarefa que deseja excluir: ")
    for tarefa in tarefas:
        if nome_tarefa == tarefa["nome"]:
            tarefas.remove(tarefa)
            print("Tarefa excluida com sucesso!")
            voltar_menu()
    else:
        print("Tarefa não encontrada")
        voltar_menu()


def opcoes():
    opcao = int(input("Insira a opção: "))
    if opcao == 1:
        criar_tarefa()
    elif opcao == 2:
        listar_tarefas()
    elif opcao == 3:
        status_tarefa()
    elif opcao == 4:
        alternar_prioridade()
    elif opcao == 5:
        excluir_tarefa()


def main():
    os.system("cls")
    nome_programa()
    tela_inicial()
    opcoes()


if __name__ == "__main__":
    main()