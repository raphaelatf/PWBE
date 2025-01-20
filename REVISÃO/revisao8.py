def contar_caracteres(s):
    dicionario = {}
    for i in s:
        if i in dicionario:
            dicionario [i] += 1
        else:
            dicionario[i] = 1
    print(dicionario)

contar_caracteres("Raphaela")
        
