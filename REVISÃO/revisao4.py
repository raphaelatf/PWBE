#CONDICIONAIS

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
n5 = float(input("Digite a quinta nota: "))

media = (n1 + n2 + n3 + n4 + n5) / 5

if media >= 5:
    print("Aprovado")
elif media >= 2.5 and 5:
    print("Recuperação")
else:
    print("Reprovado")