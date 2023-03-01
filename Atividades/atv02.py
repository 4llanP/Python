print("="*48)
print("""Faça um algoritmo para ler o salário de um funcionário e 
aumentá-Io em 15%. Após o aumento, desconte 8% de impostos.
Imprima o salário inicial, o salário com o aumento e o salário final""")
print("="*48)
def caculaSalario(x):
    z = x+x*0.15
    y = z*0.92
    return x,z,y

salario = [*caculaSalario(float(input("\nSalario atual: ")))]
print("\nSalário atual: {} \nApós aumento salárial: {} \nSalário calculado com taxas: {}\n".format(salario[0],salario[1],salario[2]))
print("="*48)