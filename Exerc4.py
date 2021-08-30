n1 = float(input("informe o valor do prêmio:"))
totalimposto = n1-((n1 * 7)/100)
pg = totalimposto-((totalimposto * 46)/100)
pg2 = pg-((pg * 32)/100)
pg3 = totalimposto - pg - pg2

print("Total do prêmio:{}\n Menos impostos = {}\n Primeiro ganhador = {}\n Segundo ganhador = {}\n Terceiro ganhador = {}".format(n1,totalimposto,pg,pg2,pg3))