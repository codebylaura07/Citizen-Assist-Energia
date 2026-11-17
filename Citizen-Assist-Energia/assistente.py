
"""Fluxo de atendimento do Citizen Assist Energia."""

import re
import time
from datetime import datetime


class Assistente:
    def __init__(self, nome, base):
        self.nome = nome
        self.base = base
        self.historico = []
        self.nota_usabilidade = None

        try:
            with open("data/historico.csv", "r", encoding="utf-8") as arquivo:
                arquivo.readline()

                for linha in arquivo:
                    campos = linha.strip().split(";")

                    if len(campos) != 8:
                        continue

                    atendimento = {
                        "data": campos[0],
                        "origem": campos[1],
                        "pergunta": campos[2],
                        "id_orientacao": campos[3],
                        "encontrou": campos[4],
                        "ajudou": campos[5],
                        "tentativas": int(campos[6]),
                        "tempo_segundos": float(campos[7])
                    }

                    self.historico.append(atendimento)

        except FileNotFoundError:
            print("Histórico ainda não encontrado. Será criado no primeiro atendimento.")

        except (OSError, ValueError):
            print("Aviso: não foi possível carregar todos os registros do histórico.")

    def perguntar(self):
        inicio = time.time()
        tentativas = 0

        while True:
            pergunta = input(
                "\nDigite sua pergunta sobre energia ou 0 para voltar: "
            ).strip()

            if pergunta == "0":
                return

            if not pergunta:
                print("Digite uma pergunta válida.")
                continue

            if "@" in pergunta or re.search(r"\d{8,}", pergunta):
                print("\nPor segurança, não envie dados pessoais.")
                print("Este atendimento não será registrado.")
                continue

            tentativas += 1
            resultados = self.base.buscar(pergunta)

            if not resultados or resultados[0][0] < 3:
                print("\nNão encontrei uma orientação adequada.")
                print("Tente outras palavras ou consulte as categorias.")

                atendimento = {
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "origem": "pergunta",
                    "pergunta": pergunta,
                    "id_orientacao": "",
                    "encontrou": "não",
                    "ajudou": "não",
                    "tentativas": tentativas,
                    "tempo_segundos": round(time.time() - inicio, 1)
                }

                self.registrar(atendimento)

                continuar = input(
                    "Deseja tentar novamente? (s/n): "
                ).strip().lower()

                while continuar not in ["s", "n"]:
                    print("Opção inválida. Digite s ou n.")
                    continuar = input(
                        "Deseja tentar novamente? (s/n): "
                    ).strip().lower()

                if continuar == "s":
                    continue

                return

            pontos, melhor_orientacao = resultados[0]

            if pontos >= 6:
                confianca = "ALTA"
            else:
                confianca = "MÉDIA"

            print(f"\nConfiança da resposta: {confianca}")

            melhor_orientacao.exibir()

            if len(resultados) > 1:
                print("\nOutras orientações relacionadas:")

                for pontos_alternativa, orientacao in resultados[1:3]:
                    print(
                        f"- {orientacao.titulo} "
                        f"({pontos_alternativa} pontos)"
                    )

            ajudou = input(
                "\nEssa orientação ajudou? (s/n): "
            ).strip().lower()

            while ajudou not in ["s", "n"]:
                print("Opção inválida. Digite s ou n.")
                ajudou = input(
                    "\nEssa orientação ajudou? (s/n): "
                ).strip().lower()

            atendimento = {
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "origem": "pergunta",
                "pergunta": pergunta,
                "id_orientacao": melhor_orientacao.id,
                "encontrou": "sim",
                "ajudou": "sim" if ajudou == "s" else "não",
                "tentativas": tentativas,
                "tempo_segundos": round(time.time() - inicio, 1)
            }

            self.registrar(atendimento)
            return

    def navegar(self):
        categorias = self.base.categorias()

        if not categorias:
            print("Nenhuma categoria disponível.")
            return

        while True:
            print("\n===== CATEGORIAS DE ENERGIA =====")

            for indice, categoria in enumerate(categorias, start=1):
                print(f"{indice} - {categoria}")

            print("0 - Voltar")

            opcao = input("Escolha uma categoria: ").strip()

            if opcao == "0":
                return

            if not opcao.isdigit() or not (1 <= int(opcao) <= len(categorias)):
                print("Opção inválida. Tente novamente.")
                continue

            categoria_escolhida = categorias[int(opcao) - 1]
            orientacoes = self.base.por_categoria(categoria_escolhida)

            while True:
                print(f"\n===== {categoria_escolhida} =====")

                for indice, orientacao in enumerate(orientacoes, start=1):
                    print(f"{indice} - {orientacao.titulo}")

                print("0 - Voltar")

                escolha = input("Escolha uma orientação: ").strip()

                if escolha == "0":
                    break

                if not escolha.isdigit() or not (1 <= int(escolha) <= len(orientacoes)):
                    print("Opção inválida. Tente novamente.")
                    continue

                inicio = time.time()
                orientacao_escolhida = orientacoes[int(escolha) - 1]

                orientacao_escolhida.exibir()

                ajudou = input(
                    "\nEssa orientação ajudou? (s/n): "
                ).strip().lower()

                while ajudou not in ["s", "n"]:
                    print("Opção inválida. Digite s ou n.")
                    ajudou = input(
                        "Essa orientação ajudou? (s/n): "
                    ).strip().lower()

                atendimento = {
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "origem": "categoria",
                    "pergunta": "",
                    "id_orientacao": orientacao_escolhida.id,
                    "encontrou": "sim",
                    "ajudou": "sim" if ajudou == "s" else "não",
                    "tentativas": 1,
                    "tempo_segundos": round(time.time() - inicio, 1)
                }

                self.registrar(atendimento)

    def registrar(self, atendimento):
        self.historico.append(atendimento)

        try:
            with open(
                "data/historico.csv", "a", encoding="utf-8"
            ) as arquivo:

                if arquivo.tell() == 0:
                    arquivo.write(
                        "data;origem;pergunta;id_orientacao;"
                        "encontrou;ajudou;tentativas;tempo_segundos\n"
                    )

                campos = [
                    atendimento["data"],
                    atendimento["origem"],
                    atendimento["pergunta"],
                    atendimento["id_orientacao"],
                    atendimento["encontrou"],
                    atendimento["ajudou"],
                    atendimento["tentativas"],
                    atendimento["tempo_segundos"]
                ]

                campos = [
                    str(campo).replace(";", ",").replace("\n", " ")
                    for campo in campos
                ]

                arquivo.write(";".join(campos) + "\n")

        except OSError:
            print("Aviso: não foi possível gravar o histórico.")

    def indicadores(self):
        total = len(self.historico)

        if total == 0:
            print("\nAinda não existem atendimentos registrados.")
            return

        encontrados = sum(
            1 for item in self.historico
            if item["encontrou"] == "sim"
        )

        ajudaram = sum(
            1 for item in self.historico
            if item["ajudou"] == "sim"
        )

        tempo_total = sum(
            float(item["tempo_segundos"])
            for item in self.historico
        )

        tentativas_total = sum(
            int(item["tentativas"])
            for item in self.historico
        )

        percentual_encontrado = (encontrados / total) * 100
        percentual_ajudou = (ajudaram / total) * 100
        tempo_medio = tempo_total / total
        tentativas_media = tentativas_total / total

        print("\n========== INDICADORES DE ENERGIA ==========")
        print(f"Total de atendimentos: {total}")
        print(f"Respostas encontradas: {percentual_encontrado:.1f}%")
        print(f"Atendimentos que ajudaram: {percentual_ajudou:.1f}%")
        print(f"Tempo médio: {tempo_medio:.1f} segundos")
        print(f"Média de tentativas: {tentativas_media:.1f}")

        if self.nota_usabilidade is not None:
            print(f"Facilidade de uso: {self.nota_usabilidade}/5")
        else:
            print("Facilidade de uso: ainda não avaliada")

        print("\nPerguntas não resolvidas:")

        nao_resolvidas = [
            item for item in self.historico
            if item["encontrou"] == "não"
        ]

        if nao_resolvidas:
            for item in nao_resolvidas:
                print(f"- {item['pergunta']}")
        else:
            print("Nenhuma pergunta não resolvida.")

        print("============================================")

    def exportar_csv(self):
        cabecalho = (
            "data;origem;pergunta;id_orientacao;"
            "encontrou;ajudou;tentativas;tempo_segundos\n"
        )

        try:
            with open(
                "data/atendimentos.csv", "w", encoding="utf-8"
            ) as arquivo:

                arquivo.write(cabecalho)

                for atendimento in self.historico:
                    campos = [
                        atendimento["data"],
                        atendimento["origem"],
                        atendimento["pergunta"],
                        atendimento["id_orientacao"],
                        atendimento["encontrou"],
                        atendimento["ajudou"],
                        atendimento["tentativas"],
                        atendimento["tempo_segundos"]
                    ]

                    campos = [
                        str(campo).replace(";", ",").replace("\n", " ")
                        for campo in campos
                    ]

                    arquivo.write(";".join(campos) + "\n")

            print("\nAtendimentos exportados para data/atendimentos.csv.")

        except OSError:
            print("Aviso: não foi possível exportar os atendimentos.")
