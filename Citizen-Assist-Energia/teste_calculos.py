from calculos_energia import carregar_dados_consumo
from calculos_energia import exibir_resumo, simular_economia
from calculos_energia import comparar_alternativas


consumo_mensal, conta_mensal = carregar_dados_consumo()

exibir_resumo(consumo_mensal, conta_mensal)

simular_economia(conta_mensal)

comparar_alternativas(consumo_mensal, conta_mensal)