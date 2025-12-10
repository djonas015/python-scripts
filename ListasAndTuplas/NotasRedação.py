notas = []
for i in range(10):
    notas.append(int(input("Adicione as notas dos alunos ")))
    notas.sort()
print(f"Notas ordenadas: {notas}")
