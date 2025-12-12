participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 

participante_removivel = input("Nome do participante a ser removido: ")
for grupo in participantes.values():
    if participante_removivel in grupo:
        grupo.remove(participante_removivel)
        print(f"Nome dos participantes: {participantes}")
