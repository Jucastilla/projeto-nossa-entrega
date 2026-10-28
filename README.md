# Análise de Dados — Projeto Nossa Entrega

## Contexto

O **Projeto Nossa Entrega** é uma iniciativa voluntária que realiza ações semanais de apoio a pessoas em situação de rua em Copacabana, no Rio de Janeiro.

Este estudo de caso foi desenvolvido a partir dos registros operacionais de participação dos voluntários e de transporte das ações, referentes ao período de **09/09/2025 a 08/09/2026**.

A base inicial continha **328 registros**, sendo **323 participações de 48 voluntários distintos** e **5 registros de ações sem entrega**.

Para preservar a identidade dos voluntários, os nomes reais foram substituídos por nomes fictícios na versão pública. Os demais registros e indicadores foram mantidos para preservar a consistência das análises.

## Objetivo

Analisar a evolução, a frequência, a recorrência e a concentração das participações dos voluntários, incluindo a entrada e o retorno de novos participantes.

Como dimensão complementar, avaliar a disponibilidade dos transportes e a distribuição das participações dos motoristas de carro.

Transformar os registros operacionais em bases analíticas e indicadores, apresentando os resultados e recomendações em um dashboard interativo para apoiar o acompanhamento do projeto.

## Desenvolvimento

### Estruturação e Carregamento dos Registros

Os dados foram coletados, organizados e estruturados a partir do controle das ações do Projeto Nossa Entrega.

A planilha de entrada foi carregada no notebook Python pela aba `Participações`, com informações sobre:

- Data da ação;
- Identificação do voluntário;
- Primeira participação;
- Função;
- Tipo de transporte;
- Quantidade de transportes na ação;
- Observações.

Os cinco registros classificados como **“Sem entrega”** foram preservados por representarem uma condição válida, mas não foram contabilizados como participações individuais.

### Inspeção e Validação dos Dados

Foram utilizados **Python, Pandas, NumPy e Matplotlib** para explorar a estrutura da base e realizar verificações de:

- Quantidade de registros e colunas;
- Tipos de dados;
- Valores ausentes;
- Categorias;
- Registros duplicados;
- Nomes com espaços excedentes;
- Relação entre tipo de transporte e função;
- Registros sem identificação de voluntário.

A validação inicial não identificou linhas duplicadas nem nomes com espaços excedentes.

Os valores ausentes encontrados estavam relacionados aos cinco registros de ações sem entrega, que não foram excluídos automaticamente.

### Tratamento e Preparação dos Dados

O tratamento foi realizado em Python, utilizando uma cópia do DataFrame de entrada.

Os procedimentos incluíram:

- Conversão da quantidade de transportes para o tipo inteiro anulável `Int64`;
- Verificação das datas inicial e final;
- Criação da variável de dia da semana;
- Validação da periodicidade das ações;
- Separação das participações individuais para os cálculos correspondentes;
- Organização de variáveis temporais;
- Criação de indicadores derivados;
- Validação das tabelas analíticas antes da exportação.

Foi verificado que os registros correspondiam a **terças-feiras**, conforme a periodicidade informada para as ações.

Na versão pública, a fonte contém nomes fictícios. Os arquivos com identificações reais não integram o repositório.

### Análise Exploratória

A análise contemplou:

- Evolução da quantidade de participantes por ação;
- Frequência e recorrência dos voluntários;
- Concentração das participações;
- Entrada e retorno de novos participantes;
- Disponibilidade e classificação dos transportes;
- Distribuição das participações dos motoristas de carro.

Para comparar a evolução da participação, as **42 ações com participação** foram divididas em três blocos cronológicos de 14 ações.

O retorno dos novos voluntários foi analisado com dois critérios: uma janela de quatro ações posteriores à entrada no notebook e o retorno observado no período disponível no dashboard.

### Preparação das Bases Analíticas

Foram construídas duas tabelas com diferentes níveis de granularidade:

- `participacoes.csv`: uma linha por participação de voluntário em cada ação, com informações de função e transporte;
- `acoes.csv`: uma linha por ação realizada com participação, com indicadores consolidados de voluntários e transportes.

As bases passaram por verificações de integridade e consistência antes da exportação para `data/processed/`, diretório utilizado pelo dashboard.

### Desenvolvimento do Dashboard

Foi desenvolvido um dashboard com **Python, Pandas, Streamlit e Plotly**, organizado em cinco páginas:

| Página | Conteúdo |
|---|---|
| Visão Geral | Indicadores do período e evolução da quantidade de participantes por ação. |
| Atuação dos Voluntários | Frequência, recorrência, concentração das participações, retorno e entrada mensal de novos voluntários. |
| Logística das Ações | Quantidade e distribuição dos transportes, participação de bicicletas e ranking dos motoristas. |
| Análise dos Resultados | Interpretações dos indicadores de participação e logística. |
| Recomendações Estratégicas | Frentes de acompanhamento baseadas nos resultados. |

## Resultados

### Panorama das Ações

| Indicador | Resultado |
|---|---|
| Ações com participação | 42 |
| Participações registradas | 323 |
| Voluntários distintos | 48 |
| Média de participantes por ação | 7,69 |
| Mediana de participantes por ação | 8 |
| Variação de participantes por ação | 4 a 10 |

### Evolução da Participação

A comparação dos três blocos cronológicos apresentou:

| Bloco | Quantidade de ações | Média de participantes |
|---|---|---|
| Primeiro | 14 | 7,64 |
| Segundo | 14 | 8,71 |
| Terceiro | 14 | 6,71 |

O segundo bloco apresentou a maior média. No terceiro, houve redução da média e maior oscilação na quantidade de participantes.

### Frequência e Concentração

Entre os 48 voluntários:

- **22 (45,8%)** participaram de apenas uma ação;
- **12 (25,0%)** participaram de 2 a 5 ações;
- **7** participaram de mais de 20 ações.

Os sete voluntários mais frequentes concentraram **192 das 323 participações**, equivalentes a aproximadamente **59,4% do total**.

Os resultados mostraram a coexistência de participações pontuais e de um grupo menor de voluntários recorrentes, responsável por parte expressiva das presenças.

### Entrada e Retorno de Novos Voluntários

Foram identificados **17 novos voluntários** pelo campo `Primeira participação?`, distinguindo a primeira participação efetiva no projeto da primeira aparição no período analisado.

As análises de retorno apresentaram:

| Critério | Voluntários considerados | Com retorno | Taxa |
|---|---|---|---|
| Retorno nas quatro ações seguintes à entrada, com janela completa | 11 | 5 | 45,5% |
| Retorno observado nos registros disponíveis no período | 17 | 6 | 35,3% |

Na análise com janela de quatro ações, seis voluntários não foram incluídos no cálculo por não possuírem quatro ações posteriores disponíveis.

**As métricas têm critérios e denominadores diferentes e não devem ser interpretadas como equivalentes.**

### Logística de Transporte

Nas 42 ações, foram identificados:

| Indicador | Resultado |
|---|---|
| Transportes registrados | 110 |
| Média de transportes por ação | 2,62 |
| Mediana de transportes por ação | 3 |
| Variação de transportes por ação | 1 a 4 |
| Ações com participação de bicicletas | 12 (28,6%) |

A conferência entre o total informado e os transportes classificados apresentou correspondência em **41 das 42 ações**.

Na ação de **25/11/2025**, foram informados três transportes, mas os registros individuais identificavam apenas um carro e uma bicicleta.

A composição dos 110 transportes ficou registrada como:

- **97 carros**;
- **12 bicicletas**;
- **1 transporte sem classificação identificada**.

O tipo do transporte não identificado não foi inferido.

### Participação dos Motoristas

Foram identificados **13 motoristas de carro distintos**, com **97 participações nessa função**.

Os dois motoristas mais frequentes concentraram **53 participações**, equivalentes a aproximadamente **54,6% do total de participações como motorista de carro**.

Esse resultado destacou a concentração da função em um número reduzido de voluntários.

### Entregas do Projeto

O projeto resultou em:

- Registros operacionais estruturados e validados;
- Notebook de preparação e análise exploratória;
- Duas bases analíticas para utilização no dashboard;
- Dashboard interativo com cinco páginas;
- Indicadores, interpretações e recomendações para acompanhamento das ações.

As análises destacaram variações na participação ao longo do período, concentração das presenças em voluntários recorrentes e concentração das participações como motorista.

Esses padrões descrevem os registros analisados e não demonstram, isoladamente, as causas das oscilações observadas.

### Recomendações Derivadas da Análise

O dashboard apresenta cinco frentes de acompanhamento:

- Planejamento das ações;
- Captação e continuidade dos voluntários;
- Distribuição dos transportes;
- Captação de recursos e parcerias locais;
- Monitoramento e melhoria contínua.

As recomendações foram apresentadas para apoiar o acompanhamento operacional, sem atribuir relações de causa e efeito não comprovadas pelos dados disponíveis.

## Habilidades Demonstradas

- Análise de dados;
- Python;
- Pandas;
- NumPy;
- Matplotlib;
- Plotly;
- Streamlit;
- DataFrames;
- Leitura e manipulação de arquivos Excel e CSV;
- Inspeção e validação de dados;
- Tratamento de valores ausentes;
- Investigação de duplicidades;
- Conversão de tipos de dados;
- Manipulação de datas;
- Criação de variáveis derivadas;
- Agrupamento e agregação de dados;
- Contagem distinta;
- Análise exploratória de dados;
- Análise temporal;
- Análise de frequência e recorrência;
- Análise de concentração;
- Análise de retorno de voluntários;
- Validação de indicadores logísticos;
- Preparação de bases analíticas;
- Exportação de arquivos CSV;
- Visualização de dados;
- Desenvolvimento de dashboards interativos;
- Indicadores e KPIs;
- Análise e interpretação de dados;
- Recomendações baseadas em dados;
- Documentação técnica.

## Arquivos do Projeto

Os arquivos estão organizados entre o notebook, as bases de dados e o código do dashboard.

### [Notebook — Análise Exploratória](https://github.com/Jucastilla/projeto-nossa-entrega/tree/main/notebook)

Notebook Jupyter contendo carregamento, inspeção, validação, tratamento e preparação dos dados, análises exploratórias e exportação das bases utilizadas no dashboard.

### [Dados Utilizados no Projeto](https://github.com/Jucastilla/projeto-nossa-entrega/tree/main/data)

A pasta contém a planilha de entrada com nomes fictícios e os arquivos processados.

A planilha está em `data/raw/`. As bases analíticas estão em `data/processed/`:

- `participacoes.csv`: registros individuais de participação;
- `acoes.csv`: indicadores consolidados por ação.

### [Dashboard — Código Streamlit](https://github.com/Jucastilla/projeto-nossa-entrega/blob/main/dashboard/app.py)

Aplicação desenvolvida em Python, Streamlit e Plotly, com cinco páginas dedicadas aos indicadores, gráficos, análises e recomendações.

### [Dashboard Interativo Online](https://projeto-nossa-entrega.streamlit.app/)

Versão pública do dashboard, com nomes fictícios para preservar a identidade dos voluntários.

## Como Executar Localmente

Com Python instalado, abra o terminal na raiz do repositório e instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Em seguida, execute a aplicação:

```bash
python -m streamlit run dashboard/app.py
```

O aplicativo utiliza os arquivos CSV disponíveis em `data/processed/`, que devem estar presentes para o carregamento correto dos indicadores.
