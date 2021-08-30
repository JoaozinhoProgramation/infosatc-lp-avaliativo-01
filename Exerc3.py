altura = float(input("Digite o valor da largura:"))
comprimento = float(input("Digite o valor da área:"))

total = (altura * comprimento)/3
tintas = total / 3.6
outrototal = tintas * 107


print("Você consegue {.2f} latas de tintas".format(outrototal))