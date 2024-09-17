def calcula(dicionario):
    total = sum(dicionario.values())
    for chave in dicionario:
        percentual = (dicionario[chave]/total) * 100
        dicionario[chave] = percentual
    return dicionario

dicionario = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}
calcula(dicionario)

for estado, percentual in dicionario.items():
    print(f"{estado}: {percentual:.2f}%")