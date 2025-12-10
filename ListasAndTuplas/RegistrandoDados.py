dados = input("Insira os dados dos alunos: ").split(", ")
for i in range(0, len(dados), 3):
    aluno1 = print(f"Nome: {dados[i]}")
    idade1 = print(f"Idade: {dados[i+1]}")
    nota1 = print(f"Nota: {dados[i+2]}")
