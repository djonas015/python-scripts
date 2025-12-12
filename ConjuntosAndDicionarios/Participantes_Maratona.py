participantes = { 

    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35 

}
listanomes = list(participantes.keys())
listaidade = list(participantes.values())
print(f"Nome dos participantes: {', '.join(listanomes)}")
print(f"Idade dos participantes: ", *listaidade, sep=", ")
for i in range(4):
    print("Participantes e suas idades:"
          f" {listanomes[i]}, {listaidade[i]} anos")
