url_user = input("Insira a url para validação: ")
if (url_user.startswith("https://")) and (url_user.endswith(".com")):
    print("Url válida")
else:
    print("Url inválida!!")
