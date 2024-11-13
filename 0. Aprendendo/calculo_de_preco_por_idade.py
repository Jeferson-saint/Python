# print do nome
print("Sistema desenvolvido por Jeferson Santos Rodrigues")

# entrada para o valor base e idade
valb = float(input("Informe o valor base do plano: "))
idade = int(input("Informe a idade do cliente: "))
valmen = 0

# cálculo do valor mensal com base no valor base e idade
if idade < 19 and idade >= 0:
    valmen = valb * (100/100)
    print(f"O valor mensal do plano é de: {valmen:,.2f}")
elif idade < 29:
    valmen = valb * (150/100)
    print(f"O valor mensal do plano é de: {valmen:,.2f}")
elif idade < 39:
    valmen = valb * (225/100)
    print(f"O valor mensal do plano é de: {valmen:,.2f}")
elif idade < 49:
    valmen = valb * (240/100)
    print(f"O valor mensal do plano é de: {valmen:,.2f}")
elif idade < 59:
    valmen = valb * (350/100)
    print(f"O valor mensal do plano é de: {valmen:,.2f}")
else:
    valmen = valb * (600/100)
    print(f"O valor mensal do plano é de: {valmen:,.2f}")
