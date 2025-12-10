import random
tentativas = 0
numerofinal = random.randint(0, 100)

print("\fVamos jogar? adivinhe um número entre 0 e 100")
while True:
    numero = int(input("\fNúmero escolhido: "))
    if numero == numerofinal:
        print("Parabéns! Voce acertou!")
        tentativas += 1
        print(f"tentativas: {tentativas}")
        break
    else:
        print("Errou!!! tente novamente")
        tentativas += 1
        print(f"tentativas: {tentativas}")
        if numero > numerofinal:
            print("Mais baixo")
        else:
            print("Mais alto")
