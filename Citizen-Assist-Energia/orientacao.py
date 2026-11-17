
"""Modelo de uma orientação da base de conhecimento sobre energia."""


class Orientacao:
    def __init__(
        self,
        id,
        categoria,
        titulo,
        palavras_chave,
        resposta,
        documentos,
        onde,
        fonte,
        verificado_em
    ):
        self.id = id
        self.categoria = categoria
        self.titulo = titulo
        self.palavras_chave = palavras_chave
        self.resposta = resposta
        self.documentos = documentos
        self.onde = onde
        self.fonte = fonte
        self.verificado_em = verificado_em

    def exibir(self):
        print("\n" + "=" * 50)
        print(self.titulo)
        print("=" * 50)
        print(f"Categoria: {self.categoria}")
        print(f"\nOrientação:\n{self.resposta}")
        print(f"\nDocumentos ou requisitos: {self.documentos}")
        print(f"Onde encontrar: {self.onde}")
        print(f"Fonte: {self.fonte}")
        print(f"Verificado em: {self.verificado_em}")
        print("\nAviso: as recomendações são estimativas e não substituem uma avaliação técnica.")
        print("=" * 50)
