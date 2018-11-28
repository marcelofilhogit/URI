peca1 = input().split(" ")
peca2 = input().split(" ")

cod1, quant1, valor1 = peca1
cod2, quant2, valor2 = peca2

cod1 = int(cod1)
quant1 = int(quant1)
valor1 = float(valor1)

cod2 = int(cod2)
quant2 = int(quant2)
valor2 = float(valor2)

total = (quant1 * valor1) + (quant2 * valor2)

print("VALOR A PAGAR: R$ %.2f" %total)
