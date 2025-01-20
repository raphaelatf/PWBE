numero = 0
maior = 0

while numero >= 0:
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero

print("O maior número é: ",maior)
