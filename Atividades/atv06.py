print("="*48)
print("""A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de 350 ml,
 garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma determinada quantidade
 de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele comprou.""")
print("="*48)

def calculaLitro(l,p,g):
    z = l*0.35 + p * 0.6 + g *2
    return float(z)
QuantidadeL = calculaLitro((float(input("Quantas latas de 350ml:"))), (float(input("Quantas garrafas de 600ml:"))), (float(input("Quantas Garrafas de 2L:"))))

print("\nFoi comprado ao todo {}l de Meia Cola!".format(QuantidadeL)) 
print("="*48)

