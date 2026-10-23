# Análise de Dados — Projeto Nossa Entrega

## Sobre o Projeto

O **Projeto Nossa Entrega** é uma iniciativa voluntária que realiza ações semanais de apoio a pessoas em situação de rua, em Copacabana, no Rio de Janeiro. Este estudo de caso organiza e analisa registros de participação de voluntários e de transporte das ações, com foco em transformar informações operacionais em indicadores úteis ao acompanhamento do projeto.

O trabalho compreende **estruturação dos registros, inspeção e validação da base, tratamento e preparação de dados, análise exploratória em Python, construção de bases analíticas e desenvolvimento de um dashboard interativo com Streamlit e Plotly**.

O período analisado vai de **09/09/2025 a 08/09/2026**. Os dados analisados são derivados de registros operacionais do Projeto Nossa Entrega.

## Privacidade dos Dados

Para preservar a identidade dos voluntários, os nomes reais foram substituídos por nomes fictícios. Os demais registros e indicadores foram mantidos para preservar a consistência das análises.

## Objetivo

Analisar a evolução, a frequência, a recorrência e a concentração das participações dos voluntários, incluindo a entrada e o retorno de novos participantes. Como dimensão complementar, avaliar a disponibilidade dos transportes e a distribuição das participações dos motoristas de carro.

A proposta é demonstrar um fluxo de trabalho em Análise de Dados, da validação da fonte até a interpretação de resultados e a apresentação de recomendações operacionais.

## Etapas Desenvolvidas

### 1. Fonte e Estrutura dos Dados

Os registros foram coletados, organizados e estruturados a partir do controle das ações do Projeto Nossa Entrega. A planilha original foi carregada no notebook Python a partir da aba **`Participações`**, com campos relacionados a data, identificação do voluntário, primeira participação, função, tipo de transporte, quantidade de transportes na ação e observações.

A base inicial contém **328 registros**: **323 participações de 48 voluntários distintos** e **5 registros referentes a ações sem entrega**. Esses cinco registros não representam participações individuais e foram preservados na base original por registrarem uma condição válida.

### 2. Exploração Inicial e Validação dos Dados

O notebook utiliza **Python, Pandas, NumPy e Matplotlib** para inspecionar dimensões, colunas, tipos de dados, valores ausentes, categorias e duplicidades.

Também foram realizadas verificações relacionadas a:

- Quantidade de registros e colunas;
- Tipos de dados;
- Valores ausentes;
- Registros duplicados;
- Nomes com espaços excedentes;
- Relação entre tipo de transporte e função;
- Registros sem identificação de voluntário.

A validação inicial não identificou linhas duplicadas nem nomes com espaços excedentes.

Os valores ausentes encontrados foram relacionados aos cinco registros classificados como **"Sem entrega"**, sem exclusão automática desses registros.

### 3. Tratamento e Preparação dos Dados

Durante a análise, as etapas de tratamento e preparação foram realizadas no Python, utilizando uma cópia do DataFrame de entrada. Na versão pública, a fonte disponibilizada contém nomes fictícios; os arquivos com identificações reais não integram este repositório.

Entre os procedimentos desenvolvidos estão:

- Conversão da quantidade de transportes para o tipo inteiro anulável `Int64`;
- Verificação das datas inicial e final da série;
- Criação da variável de dia da semana;
- Validação da periodicidade das ações;
- Separação dos registros de participação individual para os cálculos correspondentes;
- Organização de variáveis temporais;
- Criação de indicadores derivados;
- Validação das tabelas analíticas antes da exportação.

Os **328 registros** estão compreendidos entre **09/09/2025 e 08/09/2026** e correspondem a **terças-feiras**, conforme a periodicidade informada para as ações.

### 4. Análise Exploratória dos Dados

A análise exploratória foi desenvolvida em Python e contemplou diferentes perspectivas sobre a participação dos voluntários e a logística das ações.

#### Visão Geral e Evolução das Ações

Foram identificadas:

- **42 ações com participação**;
- **323 participações**;
- **48 voluntários distintos**;
- **7,69 participantes por ação**, em média;
- **8 participantes por ação**, como mediana;
- **4 a 10 participantes por ação**, como variação observada.

Para analisar a evolução da participação ao longo do período, as 42 ações foram divididas em três blocos cronológicos de 14 ações.

As médias de participação foram:

- **Primeiro bloco:** 7,64 participantes por ação;
- **Segundo bloco:** 8,71 participantes por ação;
- **Terceiro bloco:** 6,71 participantes por ação.

O terceiro bloco apresentou redução na média e maior oscilação na quantidade de participantes.

#### Frequência e Recorrência dos Voluntários

Entre os 48 voluntários identificados:

- **22 voluntários (45,8%)** participaram de apenas uma ação;
- **12 voluntários (25,0%)** participaram de 2 a 5 ações;
- **7 voluntários** participaram de mais de 20 ações.

Os sete voluntários mais frequentes registraram, juntos, **192 das 323 participações**, representando aproximadamente **59,4% do total**.

Os resultados mostram a coexistência de participações pontuais com um grupo menor de voluntários recorrentes, responsável por parte expressiva das presenças.

#### Entrada e Retorno de Novos Voluntários

Foram identificados **17 novos voluntários** a partir do campo **`Primeira participação?`**.

Essa identificação permite distinguir a primeira participação efetiva no projeto da primeira aparição de um voluntário no período analisado.

No notebook, foi desenvolvida uma análise de retorno considerando as **quatro ações seguintes à entrada**.

Dos 17 novos voluntários:

- **11** possuíam quatro ações posteriores disponíveis para acompanhamento;
- **5** retornaram dentro dessa janela;
- A taxa de retorno foi de **45,5%** entre os voluntários com janela completa.

Os seis voluntários restantes não foram incluídos nesse cálculo por não possuírem quatro ações posteriores disponíveis.

No dashboard, foi utilizado um indicador complementar de retorno, considerando os registros disponíveis no período analisado:

- **17 novos voluntários identificados**;
- **6 voluntários com retorno registrado**;
- **35,3% de retorno observado**.

As duas métricas possuem critérios e denominadores diferentes e, por isso, não devem ser interpretadas como equivalentes.

#### Logística de Transporte

Nas 42 ações analisadas, foram registrados:

- **110 transportes**;
- **2,62 transportes por ação**, em média;
- **3 transportes por ação**, como mediana;
- **1 a 4 transportes por ação**, como variação observada;
- **12 ações com participação de bicicletas (28,6%)**.

A validação dos registros identificou correspondência entre o total informado e os transportes classificados em **41 das 42 ações**.

Na ação de **25/11/2025**, foram informados três transportes, mas somente um carro e uma bicicleta estavam classificados nos registros individuais.

Por esse motivo, o total de **110 transportes registrados** difere da soma dos transportes classificados:

- **97 carros**;
- **12 bicicletas**;
- **1 transporte sem classificação identificada**.

O tipo do transporte não identificado não foi inferido, preservando a informação original.

#### Participação dos Motoristas

Foram identificados:

- **13 motoristas de carro distintos**;
- **97 participações como motorista de carro**;
- **53 participações concentradas nos dois motoristas mais frequentes**.

Essas 53 participações representam aproximadamente **54,6% das participações como motorista de carro**.

O resultado demonstra uma concentração relevante dessa função em um número reduzido de voluntários.

### 5. Preparação das Bases Analíticas

Após a análise exploratória, os dados foram organizados em duas tabelas com diferentes níveis de granularidade para utilização no dashboard interativo desenvolvido em **Streamlit e Plotly**.

As bases preparadas foram:

- **`participacoes.csv`** — uma linha por participação de voluntário em cada ação, com informações relacionadas à participação, função e transporte;
- **`acoes.csv`** — uma linha por ação realizada com participação, contendo indicadores consolidados de voluntários e transportes.

As tabelas foram submetidas a verificações de integridade e consistência antes da exportação.

Os arquivos processados são organizados em `data/processed/`, diretório utilizado pelo aplicativo Streamlit.

O **Streamlit** foi utilizado para desenvolver a aplicação interativa, enquanto o **Plotly** foi utilizado para a construção das visualizações gráficas.

### 6. Desenvolvimento do Dashboard no Streamlit

Foi desenvolvido um dashboard interativo utilizando **Python, Pandas, Streamlit e Plotly**, com o objetivo de apresentar os principais indicadores, análises e recomendações relacionados ao Projeto Nossa Entrega.

O dashboard foi organizado em **cinco páginas**.

#### Visão Geral

Apresenta os principais indicadores do período analisado:

- **42 ações realizadas com participação**;
- **323 participações registradas**;
- **48 voluntários distintos**;
- **7,7 participantes por ação**, em média.

A página também apresenta a evolução da quantidade de participantes ao longo das ações.

#### Atuação dos Voluntários

Apresenta indicadores e visualizações relacionados à frequência e à recorrência dos participantes.

Entre os resultados apresentados estão:

- **22 voluntários com apenas uma participação**;
- **59,4% das participações concentradas nos sete voluntários mais frequentes**;
- **35,3% de retorno observado entre os novos voluntários**;
- Ranking de frequência dos voluntários;
- Evolução mensal da entrada de novos participantes.

#### Logística das Ações

Apresenta os principais indicadores relacionados ao transporte:

- **110 transportes registrados**;
- **12 ações com bicicleta**;
- **13 motoristas de carro distintos**;
- Distribuição dos transportes classificados entre carros e bicicletas;
- Ranking de participação dos motoristas.

#### Análise dos Resultados

Reúne interpretações dos indicadores apresentados no dashboard.

As análises contemplam:

- Evolução e regularidade das ações;
- Frequência e concentração das participações;
- Entrada e retorno de novos voluntários;
- Disponibilidade e distribuição dos transportes;
- Participação dos motoristas.

#### Recomendações Estratégicas

Apresenta cinco frentes de acompanhamento baseadas nos resultados encontrados:

- Planejamento das ações;
- Captação e continuidade dos voluntários;
- Distribuição dos transportes;
- Captação de recursos e parcerias locais;
- Monitoramento e melhoria contínua.

As recomendações têm como finalidade apoiar o acompanhamento operacional do projeto, sem atribuir relações de causa e efeito que não possam ser comprovadas pelos dados disponíveis.

### 7. Análise dos Resultados

A análise evidencia variações na quantidade de participantes ao longo do período, com maior média no segundo bloco de ações e redução no terceiro.

A distribuição das participações também apresenta concentração relevante. Dos 48 voluntários identificados, **22 participaram apenas uma vez**, enquanto sete voluntários concentraram **59,4% das participações**.

Em relação à entrada de novos participantes, foram identificados **17 voluntários classificados como novos**. O acompanhamento do retorno demonstrou a importância de considerar a janela de observação, principalmente para participantes que ingressaram próximo ao encerramento do período analisado.

Na logística, foram registrados **110 transportes**, com participação de bicicletas em 12 ações. A análise dos motoristas mostrou que duas pessoas concentraram **54,6% das participações nessa função**.

Os resultados indicam pontos relevantes para o acompanhamento da participação dos voluntários e da organização dos transportes.

Entretanto, as análises descrevem padrões observados nos registros e não demonstram, isoladamente, as causas das oscilações identificadas.

### 8. Conclusões

O projeto permitiu transformar registros operacionais de uma iniciativa voluntária em bases estruturadas e indicadores para acompanhamento das atividades.

Com **Python e Pandas**, foram realizadas etapas de inspeção, validação, tratamento, preparação e análise exploratória dos dados.

As bases processadas foram utilizadas para o desenvolvimento de um **dashboard interativo em Streamlit e Plotly**, organizado em cinco páginas, com indicadores, gráficos, análises e recomendações relacionadas à participação dos voluntários e à logística das ações.

Os resultados destacam três aspectos relevantes:

- Variação da quantidade de participantes ao longo do período;
- Concentração das participações em um grupo de voluntários recorrentes;
- Concentração das participações como motorista em um número reduzido de voluntários.

O desenvolvimento do projeto reforça a importância da qualidade dos dados, da definição de critérios consistentes para os indicadores e da comunicação dos resultados para apoiar o acompanhamento e a organização das atividades.

## Habilidades Demonstradas

- Análise de Dados
- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Streamlit
- DataFrames
- Leitura e Manipulação de Arquivos Excel e CSV
- Inspeção e Validação de Dados
- Tratamento de Valores Ausentes
- Investigação de Duplicidades
- Conversão de Tipos de Dados
- Manipulação de Datas
- Criação de Variáveis Derivadas
- Agrupamento e Agregação de Dados
- Contagem Distinta
- Análise Exploratória de Dados
- Análise Temporal
- Análise de Frequência e Recorrência
- Análise de Concentração
- Análise de Retorno de Voluntários
- Validação de Indicadores Logísticos
- Preparação de Bases Analíticas
- Exportação de Arquivos CSV
- Visualização de Dados
- Desenvolvimento de Dashboards Interativos
- Indicadores e KPIs
- Análise e Interpretação de Dados
- Recomendações Baseadas em Dados
- Documentação Técnica

## Arquivos do Projeto

A organização prevista para o repositório público é:

```text
projeto-nossa-entrega/
├── assets/
│   └── logo_nossa_entrega.png
├── dashboard/
│   └── app.py
├── data/
│   ├── processed/
│   │   ├── acoes.csv
│   │   └── participacoes.csv
│   └── raw/
│       └── dados_nossa_entrega.xlsx
├── notebook/
│   └── [notebook de análise, após publicação]
├── README.md
└── requirements.txt
```

### Notebook

A pasta `notebook/` é destinada ao notebook Jupyter com carregamento, inspeção, validação, tratamento, preparação e análise exploratória dos dados. O nome do arquivo deve ser conferido no repositório quando for publicado. Antes da publicação, também é necessário revisar as saídas salvas das células para evitar a exposição de nomes reais.

### Dados

- **`data/raw/`** — versão revisada da planilha de entrada, com nomes fictícios. A inclusão pública deve ocorrer somente após conferência do arquivo.
- **`data/processed/participacoes.csv`** — uma linha por participação individual, com função e transporte.
- **`data/processed/acoes.csv`** — uma linha por ação com indicadores consolidados.

As duas bases CSV alimentam o dashboard.

### Dashboard

- **`dashboard/app.py`** — aplicativo Streamlit com as cinco páginas, indicadores, gráficos, análises e recomendações.
- **`assets/logo_nossa_entrega.png`** — identidade visual utilizada na aplicação.
- **`requirements.txt`** — dependências necessárias à execução.

### Dashboard Online — Streamlit

O objetivo desta versão é disponibilizar publicamente o dashboard pelo **Streamlit Community Cloud**, utilizando os dados revisados com nomes fictícios.

**Link público:** será incluído após a publicação e a confirmação de que o aplicativo está funcionando.

## Como Executar Localmente

Com Python instalado, abra o terminal na **raiz do repositório** e execute:

```bash
python -m pip install -r requirements.txt
python -m streamlit run dashboard/app.py
```

O aplicativo utiliza os arquivos CSV de `data/processed/`. Para funcionar corretamente, esses arquivos devem estar presentes nos caminhos indicados.
