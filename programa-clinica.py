
print("Programa Clinica por Jeferson Santos Rodrigues - 0210972223001")

valtotal = 0

while True:
    sex = input("Qual o seu sexo? M-Masculino F-Feminino \n").upper()
    if sex == 'M'or sex == 'F':
        break
    else:
        print("Insira uma opção válida!")
        continue

while True:

    if sex == 'M':
        opt = input("Qual exame deseja realizar? 1-RaioX 2-Exame de Sangue 3-Espermograma\n")
    elif sex == 'F':
        opt = input("Qual exame deseja realizar? 1-RaioX 2-Exame de Sangue\n")

    if opt == '1':
        valtotal += 300.00
    elif opt == '2':
        valtotal += 150.00
    elif opt == '3':
        valtotal += 250.00
    else:
        print("Insira uma opção válida!")

    cont = input("Deseja realizar outro exame? S-Sim N-Não\n").upper()

    if cont == 'S':
        continue
    elif cont == 'N':
        break
    else:
        print("Insira uma opção válida!")

taxfix = 250.00

valfinal = valtotal + taxfix

print(f"O valor total da consulta é {valfinal:,.2f}")
