import re

cpf = input("Insira o cpf no formato correto XXX.XXX.XXX-XX: ")
if re.fullmatch(r'(\d{3})\.(\d{3})\.(\d{3})\-(\d{2})', cpf):
    print("Formato válido")
else:
    print("Formato inválido")
