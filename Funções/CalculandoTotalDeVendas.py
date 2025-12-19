def calculando_vendas(valores_venda):
    soma = sum(int(num) for num in valores_venda)
    return f"Total de vendas foi R${soma}"


valores_venda = (input("Digite os valores das vendas: ").split(" "))
resultado = calculando_vendas(valores_venda)
print(resultado)
