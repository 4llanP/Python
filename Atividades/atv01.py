print("="*48)
print("""A padaria Hotpão vende uma certa quantidade de pães franceses
e uma quantidade de broas a cada dia. Cada pãozinho custa R$ 0,12
e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto
arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar
numa conta de poupança (10% do total arrecadado). Você foi contratado
para fazer os cálculos para o dono. Com base nestes fatos, faça
um algoritmo para ler as quantidades de pães e de broas, e depois
calcular os dados solicitados.""")
print("="*48)

def CaculaTotal(x,y):
    z = (x*0.12)+(y*1.5)
    w = z*0.1
    return x,y,z,w

precos = [*CaculaTotal(float(input("\nquantidade de pães vendidos: ")), float(input("quantidade de broas venidas: ")))]

print("""\n{:.0f} pães
{:.0f} broas
Total = {}
10% = {}\n""".format(precos[0], precos[1],precos[2], precos[3]))
print("="*48)