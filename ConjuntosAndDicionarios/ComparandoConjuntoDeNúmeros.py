equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}
tarefa_removivel = input("Insira a tarefa que deseja remover: ")
equipe_a.discard(tarefa_removivel)
equipe_b.discard(tarefa_removivel)
lista_atualizada = equipe_a.union(equipe_b)
print(f"{lista_atualizada}")
