entrada = input("Insira as notas dos alunos: ").split(", ")
notas_alunos = [float(nota) for nota in entrada]
nota_final = sum(notas_alunos) / len(notas_alunos)
print(f"Média final: {nota_final}")
