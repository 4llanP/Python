print("="*48)
print("""Três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de um bar. Faça um
 algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar, mas faça com que
 Carlos e André não paguem centavos. Ex: uma conta de R$101,53 resulta em R$33,00 para Carlos,
 R$33,00 para André e R$35,53 para Felipe.""")
print("="*48)

def calculo(x):
    z = x//3
    y = z + x%3
    return x, z, y

valores = [*calculo(float(input("\ninforme o valor a ser pago: ")))]
print("\nCarlos e André pagam: {} cada\nFelipe paga: {}\n".format(valores[1],valores[2]))
print("="*48)