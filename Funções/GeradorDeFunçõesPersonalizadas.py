def desconto(porcentagem):

    def valor(valor_produto):
        return valor_produto * (1 - porcentagem/100)
    return valor


desconto_porcento = float(input("Qual a porcentagem de desconto?: "))
calculo = desconto(desconto_porcento)
valor_final_produto = float(input("Qual o valor total do produto? R$ "))
resultado = calculo(valor_final_produto)
print(f"O valor final com {desconto_porcento}% de desconto é: R$ {resultado:.2f}")
