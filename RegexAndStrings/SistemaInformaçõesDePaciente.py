import re

paciente = input("Digite o nome completo e o ano de nascimento do paciente: ")
formatacao_nome = re.findall(r'\b[a-zA-Z]\w*', paciente)[0]
formatacao_sobrenome = re.findall(r'\b[a-zA-Z]\w*', paciente)[-1]
formatacao_data = re.findall(r'\d{4}+', paciente)[0]
print(f"Nome: {formatacao_nome}")
print(f"Sobrenome: {formatacao_sobrenome}")
print(f"Data: {formatacao_data}")
