# Citizen Assist Energia

**Global Solution 2026.2 — FIAP**  
**Disciplina:** Soluções em Energias Renováveis e Sustentáveis

## 1. Objetivo

O Citizen Assist Energia é uma versão independente do Citizen Assist AI, desenvolvida para oferecer orientações sobre consumo consciente de energia elétrica, eficiência energética e fontes renováveis.

O projeto busca ajudar o usuário a compreender seu consumo de energia, conhecer alternativas para economizar e comparar soluções energéticas.

## 2. Público-alvo e cenário analisado

O público-alvo definido para o estudo é o de jovens trabalhadores que desejam compreender e reduzir os gastos com energia elétrica em suas residências.

Para a análise, foi criado um cenário hipotético de uma residência localizada em São Paulo - SP.

Dados utilizados:

- Consumo mensal: 250 kWh.
- Conta mensal estimada: R$ 220,00.
- Consumo anual: 3.000 kWh.
- Despesa anual: R$ 2.640,00.
- Custo médio efetivo estimado: R$ 0,88/kWh.

Os dados são estimativas acadêmicas e não representam uma residência real ou uma tarifa oficial de energia elétrica.

## 3. Funcionalidades

O sistema possui as seguintes funcionalidades:

- Consulta de informações sobre energia por meio de perguntas.
- Navegação pelas categorias da base de conhecimento.
- Registro do histórico de atendimentos.
- Consulta de indicadores de utilização.
- Exportação dos atendimentos para arquivo CSV.
- Consulta do consumo mensal e anual.
- Simulação de economia com diferentes percentuais de redução.
- Comparação entre eficiência energética e energia solar fotovoltaica.
- Dimensionamento preliminar de sistema solar antes e depois da redução do consumo.

## 4. Estrutura do projeto

```text
Citizen-Assist-Energia/
│
├── README.md
├── main.py
├── orientacao.py
├── base_conhecimento.py
├── assistente.py
├── calculos_energia.py
├── teste_calculos.py
│
├── data/
│   ├── base_conhecimento_energia.csv
│   ├── dados_consumo.csv
│   ├── historico.csv
│   └── atendimentos.csv
│
└── analise/
    ├── calculos.md
    ├── comparacao_alternativas.md
    ├── fontes.md
    └── testes.md
```

## 5. Tecnologias utilizadas

- Python 3.
- Arquivos CSV para armazenamento de informações e registros.
- Biblioteca padrão `csv` do Python.
- GitHub para versionamento e publicação do projeto.

## 6. Como executar

1. Instale o Python 3.
2. Abra a pasta do projeto no Visual Studio Code.
3. Abra o terminal na pasta principal.
4. Execute o comando:

```bash
python main.py
```

Não são necessárias bibliotecas externas para executar a versão atual.

## 7. Análise energética

O estudo considera três alternativas:

1. Eficiência energética: redução hipotética de 10% no consumo mensal.
2. Energia solar fotovoltaica: dimensionamento preliminar de um sistema para geração própria.
3. Fornecimento convencional: manutenção do fornecimento atual da distribuidora.

A simulação de eficiência energética apresenta os seguintes resultados:

- Consumo original: 250 kWh/mês.
- Redução estimada: 25 kWh/mês.
- Novo consumo: 225 kWh/mês.
- Economia estimada: R$ 22,00/mês.
- Economia anual estimada: R$ 264,00.

Para a energia solar, foram utilizadas referências da Empresa de Pesquisa Energética (EPE):

- Geração estimada: 120 kWh/mês por kWp instalado.
- Potência estimada antes da eficiência: 2,08 kWp.
- Potência estimada após a eficiência: 1,88 kWp.
- Investimento estimado antes da eficiência: R$ 6.250,00 a R$ 14.583,33.
- Investimento estimado após a eficiência: R$ 5.625,00 a R$ 13.125,00.

Os valores são estimativas para fins acadêmicos e dependem das condições reais de instalação.

## 8. Integração ao assistente

A análise energética foi incorporada ao Citizen Assist Energia por meio de funcionalidades em Python.

O usuário pode consultar seus dados de consumo, simular economias e comparar alternativas diretamente pelo menu principal.

Os dados de consumo são carregados automaticamente do arquivo `data/dados_consumo.csv`, permitindo alterações sem modificar diretamente o código-fonte.

A base de conhecimento utiliza arquivos CSV para armazenar orientações e informações relacionadas à sustentabilidade e ao consumo consciente.

## 9. Testes realizados

Durante o desenvolvimento, foram realizados testes das seguintes funcionalidades:

- Carregamento da base de conhecimento.
- Consulta de informações por perguntas.
- Navegação por categorias.
- Registro do histórico de atendimentos.
- Consulta de indicadores.
- Exportação dos atendimentos para CSV.
- Cálculos de consumo mensal e anual.
- Simulação de economia.
- Leitura dos dados diretamente do arquivo CSV.
- Comparação das alternativas energéticas.
- Dimensionamento solar antes e depois da redução de consumo.

Os testes iniciais das funcionalidades foram executados com resultados compatíveis com os valores esperados.

Os testes com usuários externos e os respectivos comentários e ajustes deverão ser documentados após sua realização.

## 10. Limitações

- O cenário residencial utiliza dados hipotéticos.
- A redução de consumo de 10% é uma premissa de simulação, não uma garantia.
- Os custos de instalação solar são estimativas de referência.
- A geração real depende das condições do imóvel e da instalação.
- A compensação de energia e os custos de disponibilidade seguem as regras aplicáveis da ANEEL.
- As simulações não substituem avaliações técnicas ou orçamentos comerciais.
- A base de conhecimento possui limitações e pode não contemplar todas as situações.

## 11. Referências

- **Empresa de Pesquisa Energética (EPE):** Plano Decenal de Expansão de Energia 2036 — Caderno de Eficiência Energética e Recursos Energéticos Distribuídos, página 23.  
  https://epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-982/topico-851/PDE%202036_Caderno%20Efici%C3%AAncia%20e%20RED_v1_2026-11-04.pdf

- **Agência Nacional de Energia Elétrica (ANEEL):** Micro e Minigeração Distribuída.  
  https://www.gov.br/aneel/pt-br/assuntos/geracao-distribuida

- **Brasil:** Lei nº 14.300, de 6 de janeiro de 2022 — Marco Legal da Microgeração e Minigeração Distribuída.  
  https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm

## 12. Entrega acadêmica

**Projeto:** Citizen Assist Energia  
**Instituição:** FIAP  
**Global Solution:** 2026.2

- Vídeo técnico no YouTube: a inserir.
- Integrantes: Laura Godoy Callegari rm 569181
               Mariana Dreset Carbollan rm 569207

