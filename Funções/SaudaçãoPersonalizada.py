def saudacao():
    horario = int(input("Digite a hora atual: "))
    if horario < 12:
        return "Bom dia"
    elif horario < 18:
        return "Boa tarde"
    else:
        return "Boa noite!"
 

print(saudacao())