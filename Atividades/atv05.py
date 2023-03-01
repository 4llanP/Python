print("="*48)
print("""A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra.
Faça um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um determinado
funcionário. Considere que o salário líquido é igual ao salário bruto descontando-se 10% de
impostos.""")
print("="*48)

def calculo(x,y):
    z = (x*10)+(y*15)
    return z

salario = [calculo(float(input("\nHora de trabalho normal: ")),float(input("Hora de trabalho extra: ")))]
print("\nSalário total: {}\nSalário após impostos: {}\n".format(salario[0],salario[0]*0.9))
print("="*48)
