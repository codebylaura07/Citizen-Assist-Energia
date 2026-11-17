"""Ponto de entrada do Citizen Assist Energia."""

from base_conhecimento import BaseConhecimento
from assistente import Assistente
from calculos_energia import (
    carregar_dados_consumo,
    exibir_resumo,
    simular_economia,
    comparar_alternativas
)

def main():
    base = BaseConhecimento("data/base_conhecimento_energia.csv")
    base.carregar()

    assistente = Assistente("Citizen Assist Energia", base)

    while True:
        print("\n======================================")
        print("       CITIZEN ASSIST ENERGIA")
        print("======================================")
        print("1 - Fazer uma pergunta sobre energia")
        print("2 - Navegar por categorias")
        print("3 - Consultar indicadores")
        print("4 - Exportar atendimentos")
        print("5 - Consultar consumo e simular economia")
        print("6 - Comparar alternativas de energia")
        print("0 - Sair")
        print("======================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            assistente.perguntar()

        elif opcao == "2":
            assistente.navegar()

        elif opcao == "3":
            assistente.indicadores()

        elif opcao == "4":
            assistente.exportar_csv()

        elif opcao == "5":
            consumo_mensal, conta_mensal = carregar_dados_consumo()

            exibir_resumo(consumo_mensal, conta_mensal)
            simular_economia(conta_mensal)

        elif opcao == "6":
            consumo_mensal, conta_mensal = carregar_dados_consumo()

            comparar_alternativas(consumo_mensal, conta_mensal)

        elif opcao == "0":
            while True:
                nota = input(
                    "\nDe 1 a 5, como você avalia a facilidade de uso? "
                ).strip()

                if nota in ["1", "2", "3", "4", "5"]:
                    assistente.nota_usabilidade = int(nota)
                    break

                print("Nota inválida. Digite um número de 1 a 5.")

            print("\nObrigado por utilizar o Citizen Assist Energia!")

            assistente.indicadores()
            break

        else:
            print("\nOpção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()
