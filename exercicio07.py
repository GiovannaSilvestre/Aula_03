qtdLitros = float(input("Quantos litros você abasteceu?"))
tipo = input ("Qual é o combustível?\n"
            "G para gasolina\n"
            "E para etanol\n")
vGas = 5.8
vEta = 4.9

if tipo =="G" or tipo == "g":
    valorG = qtdLitros*vGas
    print(f"Você abasteceu {qtdLitros} litros"
          f" e gastou R${valorG:.2f}")

elif tipo =="E" or tipo == "e":
    valorE = qtdLitros*vEta
    print(f"Você abasteceu {qtdLitros} litros"
          f" e gastou R${valorE:.2f}")