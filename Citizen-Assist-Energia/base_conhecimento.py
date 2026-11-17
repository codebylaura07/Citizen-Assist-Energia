
"""Carregamento, organização e busca na base de conhecimento de energia."""

import re
import unicodedata

from orientacao import Orientacao


def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )
    texto = re.sub(r"[^\w\s]", " ", texto)
    return texto


class BaseConhecimento:
    def __init__(self, caminho):
        self.caminho = caminho
        self.orientacoes = []

    def carregar(self):
        self.orientacoes = []

        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:

                cabecalho = arquivo.readline().strip().split(";")

                if len(cabecalho) != 9:
                    print("Aviso: formato do arquivo CSV inválido.")
                    return

                for linha in arquivo:
                    linha = linha.strip()

                    if not linha:
                        continue

                    campos = linha.split(";")

                    if len(campos) != 9:
                        print("Aviso: uma linha do CSV está inválida.")
                        continue

                    id = campos[0].strip()
                    categoria = campos[1].strip()
                    titulo = campos[2].strip()
                    palavras_chave = campos[3].strip().split("|")
                    resposta = campos[4].strip()
                    documentos = campos[5].strip().split("|")
                    onde = campos[6].strip()
                    fonte = campos[7].strip()
                    verificado_em = campos[8].strip()

                    orientacao = Orientacao(
                        id,
                        categoria,
                        titulo,
                        palavras_chave,
                        resposta,
                        documentos,
                        onde,
                        fonte,
                        verificado_em
                    )

                    self.orientacoes.append(orientacao)

        except FileNotFoundError:
            print("Aviso: arquivo da base de conhecimento não encontrado.")

        except OSError:
            print("Aviso: não foi possível acessar o arquivo CSV.")

    def categorias(self):
        lista_categorias = []

        for orientacao in self.orientacoes:
            if orientacao.categoria not in lista_categorias:
                lista_categorias.append(orientacao.categoria)

        return lista_categorias

    def por_categoria(self, categoria):
        resultado = []

        for orientacao in self.orientacoes:
            if orientacao.categoria == categoria:
                resultado.append(orientacao)

        return resultado

    def pontuar(self, pergunta, orientacao):
        pergunta_normalizada = normalizar(pergunta)
        titulo_normalizado = normalizar(orientacao.titulo)

        palavras_pergunta = pergunta_normalizada.split()
        palavras_titulo = titulo_normalizado.split()

        pontos = 0

        for palavra_chave in orientacao.palavras_chave:
            palavra_normalizada = normalizar(palavra_chave).strip()

            if palavra_normalizada:
                trecho = " " + palavra_normalizada + " "

                if trecho in " " + pergunta_normalizada + " ":
                    pontos += 3

        for palavra in set(palavras_pergunta):
            if len(palavra) >= 4 and palavra in palavras_titulo:
                pontos += 1

        return pontos

    def buscar(self, pergunta):
        resultados = []

        for orientacao in self.orientacoes:
            pontos = self.pontuar(pergunta, orientacao)

            if pontos > 0:
                resultados.append((pontos, orientacao))

        resultados.sort(key=lambda item: item[0], reverse=True)

        return resultados
