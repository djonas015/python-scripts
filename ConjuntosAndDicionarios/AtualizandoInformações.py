estoque = { 

    "Caderno universitário": 50, 

    "Caneta azul": 120, 

    "Borracha branca": 30 

} 

produto_atualizado = input("Insira o nome do produto a ser atualizado: ")
nova_quantidade = int(input("Insira a nova quantidade: "))
if produto_atualizado in estoque:
    estoque[produto_atualizado] = nova_quantidade
print(estoque)
    
