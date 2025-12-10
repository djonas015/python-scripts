permissoes = {"leitura", "escrita", "execução", "compartilhamento"}
solicitacao = set(input("Permissões solicitadas: ").split(", "))
comparativo = solicitacao.intersection(permissoes)
if comparativo == solicitacao:
    print("As permissões solicitadas fazem parte das permissões principais.")
else:
    print("As permissões solicitadas não fazem parte das permissões principai")
