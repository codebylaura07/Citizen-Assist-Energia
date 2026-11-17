"""Cálculos de consumo e economia de energia elétrica."""
import csv

def calcular_consumo_anual(consumo_mensal):
    return consumo_mensal * 12


def calcular_custo_anual(conta_mensal):
    return conta_mensal * 12


def calcular_custo_medio_kwh(conta_mensal, consumo_mensal):
    if consumo_mensal <= 0:
        return 0

    return conta_mensal / consumo_mensal


def calcular_economia(percentual, conta_mensal):
    economia = conta_mensal * (percentual / 100)
    return economia


def exibir_resumo(consumo_mensal, conta_mensal):
    consumo_anual = calcular_consumo_anual(consumo_mensal)
    custo_anual = calcular_custo_anual(conta_mensal)
    custo_kwh = calcular_custo_medio_kwh(
        conta_mensal, consumo_mensal
    )

    print("\n======================================")
    print("       RESUMO DE CONSUMO DE ENERGIA")
    print("======================================")
    print(f"Consumo mensal: {consumo_mensal:.1f} kWh")
    print(f"Consumo anual: {consumo_anual:.1f} kWh")
    print(f"Conta mensal: R$ {conta_mensal:.2f}")
    print(f"Despesa anual: R$ {custo_anual:.2f}")
    print(f"Custo médio efetivo: R$ {custo_kwh:.2f}/kWh")
    print("======================================")


def simular_economia(conta_mensal):
    print("\n===== SIMULAÇÃO DE ECONOMIA =====")

    for percentual in [5, 10, 15, 20, 25]:
        economia_mensal = calcular_economia(
            percentual, conta_mensal
        )

        economia_anual = economia_mensal * 12

        print(
            f"Redução de {percentual}%: "
            f"R$ {economia_mensal:.2f}/mês | "
            f"R$ {economia_anual:.2f}/ano"
        )

def carregar_dados_consumo(caminho="data/dados_consumo.csv"):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")

        dados = next(leitor)

        consumo_mensal = float(dados["consumo_kwh_mes"])
        conta_mensal = float(dados["conta_mensal_reais"])

        return consumo_mensal, conta_mensal

def comparar_alternativas(consumo_mensal, conta_mensal):
    print("\n======================================")
    print("       COMPARAÇÃO DE ALTERNATIVAS")
    print("======================================")

    # Alternativa 1: eficiência energética
    reducao = 10

    economia = calcular_economia(reducao, conta_mensal)
    consumo_reduzido = consumo_mensal * (1 - reducao / 100)

    print("\n1 - EFICIÊNCIA ENERGÉTICA")
    print(f"Redução considerada: {reducao}%")
    print(f"Consumo após redução: {consumo_reduzido:.1f} kWh/mês")
    print(f"Economia estimada: R$ {economia:.2f}/mês")
    print(f"Economia anual: R$ {economia * 12:.2f}")

    # Alternativa 2: energia solar
    geracao_por_kwp = 120
    custo_minimo_kwp = 3000
    custo_maximo_kwp = 7000

    sistema_atual = consumo_mensal / geracao_por_kwp
    sistema_reduzido = consumo_reduzido / geracao_por_kwp

    investimento_atual_min = sistema_atual * custo_minimo_kwp
    investimento_atual_max = sistema_atual * custo_maximo_kwp

    investimento_reduzido_min = sistema_reduzido * custo_minimo_kwp
    investimento_reduzido_max = sistema_reduzido * custo_maximo_kwp

    print("\n2 - ENERGIA SOLAR FOTOVOLTAICA")
    print(f"Sistema antes da economia: {sistema_atual:.2f} kWp")
    print(f"Sistema após a economia: {sistema_reduzido:.2f} kWp")

    print("\nInvestimento estimado antes da economia:")
    print(f"R$ {investimento_atual_min:.2f} a R$ {investimento_atual_max:.2f}")

    print("\nInvestimento estimado após a economia:")
    print(f"R$ {investimento_reduzido_min:.2f} a R$ {investimento_reduzido_max:.2f}")

    print("\nObservação: valores estimados para fins acadêmicos.")
    print("A geração real depende das condições do imóvel.")
    print("A conta de luz não será necessariamente zerada.")

    print("\n======================================")