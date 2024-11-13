# print do nome e do cardápio
print("Bem-Vindo a Pizzaria do Jeferson Santos Rodrigues")
print("")
print("-----------------Cardápio-----------------")
print("")
print("-- | Tamanho | Pizza Salgada(PS) | Pizza Doce(PD) | --")
print("-- |    P    |     R$ 30.00      |     R$ 34.00   | --")
print("-- |    M    |     R$ 45.00      |     R$ 48.00   | --")
print("-- |    G    |     R$ 60.00      |     R$ 66.00   | --")
print("")

# acumulador
preco = 0

# laço de repetição do cardápio
while True:

    # entrada do sabor
    sabor = input("Entre com o sabor desejado (PS/PD): ").upper()

    # definicao do sabor para o print
    if sabor == "PS":
        sb = "Pizza Salgada"
    elif sabor == "PD":
        sb = "Pizza Doce"
    else:
        print("Sabor inválido. Tente novamente")
        continue

    # entrada do tamanho
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()

    # calculo do valor e valor atual
    if sabor == "PS" and tamanho == "P":
        precoatual = 30.00
        preco += 30.00
    elif sabor == "PS" and tamanho == "M":
        precoatual = 45.00
        preco += 45.00
    elif sabor == "PS" and tamanho == "G":
        precoatual = 60.00
        preco += 60.00
    elif sabor == "PD" and tamanho == "P":
        precoatual = 34.00
        preco += 34.00
    elif sabor == "PD" and tamanho == "M":
        precoatual = 48.00
        preco += 48.00
    elif sabor == "PD" and tamanho == "G":
        precoatual = 66.00
        preco += 66.00
    else:
        print("Tamanho inválido. Tente novamente")
        continue

    # print do preco atual e sabor
    print(f"Você pediu uma {sb} no tamanho {tamanho}: R$ {precoatual:,.2f}")

    # opção de continuar
    opt = input("Deseja mais alguma coisa? (S/N): ").upper()

    # definição se o loop acaba ou continua e print do total
    if opt == "S":
        continue
    elif opt == "N":
        print(f"O valor total a ser pago: R$ {preco:,.2f}")
        break
    else:
        print("Opção Inválida")
