nome = input()
salario = float(input())
totalVend = float(input())

comissao = totalVend * 0.15
total = salario + comissao

print("TOTAL = R$ %0.2f"%total)
