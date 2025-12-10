texto1 = set(input("texto 1: ").split())
texto2 = set(("O céu azul anuncia um dia de sol intenso").split())
comuns = texto1.intersection(texto2)
print(f"{comuns}")
