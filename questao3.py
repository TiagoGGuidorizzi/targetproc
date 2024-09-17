import json

def lerjson(arquivo_json):
    with open(arquivo_json, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados['faturamento']

def calcular_faturamento(faturamento_diario):
    faturamento = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]
    menor = min(faturamento)
    maior = max(faturamento)
    
    media_mensal = sum(faturamento) / len(faturamento)
    
    dias = sum(1 for valor in faturamento if valor > media_mensal)
    
    return menor, maior, dias

faturamento_diario = lerjson('dados.json')

menor, maior, dias = calcular_faturamento(faturamento_diario)

print(f"Menor valor de faturamento: R$ {menor}")
print(f"Maior valor de faturamento: R$ {maior}")
print(f"Número de dias com faturamento acima da média mensal: {dias}")
