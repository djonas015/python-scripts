def idade():
    nascimento = int(input("Ano de nascimento: "))
    ano_atual = int(input("Ano atual: "))
    idade_correta = ano_atual - nascimento
    return f"{idade_correta} anos"


print(idade())
