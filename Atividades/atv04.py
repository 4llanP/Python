print("="*48)
print("""Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit. Faça um
 algoritmo para ler uma temperatura Celsius e imprimi-Ia em Fahrenheit (pesquise como fazer
 este tipo de conversão).""")
print("="*48)

def calculo(x):
    z = x*1.8+32
    return z

print("\n°F = {}\n".format(calculo(float(input("\nTemperatura em °C: ")))))
print("="*48)