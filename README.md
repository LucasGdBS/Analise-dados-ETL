<!-- markdownlint-disable MD029 -->
# Desafio

## Tecnologias utilizadas

- Python - 3.12
- PostgreSQL
- Metabase
- Docker

## Como executar o projeto

1. Instale os requisitos do projeto

```bash
pip install -r requirements.txt
```

### Configuração do kaggle

1. Execute o comando do CLI do kaggle para que ele crie o diretorio no seu computador

```bash
kaggle
```

2. Crie sua API key no Kaggle. Isso irá gerar um arquivo Json

3. Coloque o arquivo chamado kaggle.json em `~/.kaggle/kaggle.json` no Linux, OSX, e outros sistemas operacionais baseados em UNIX, e em `C:\Users\<Windows-usernamekaggle\kaggle.json\.` no Windows.

### Configurando o banco de dados

1. Certifique-se de ter o PostgreSQL instalado e rodando na sua máquina (Ou um Docker).

2. Crie um banco de dados no Postgresql

3. Crie um arquivo `.env` e adicione as variaveis de conexão, como no exemplo dado em `.env.example`.

### Executando o projeto

1. Basta executar o arquivo main.py na raiz do projeto.

### Configurando o metabase

1. Instale o metabase na sua máquina (Ou em um docker)

2. Acesse o metabase através do navegador na rota `localhost:3000`

2. Conecte o banco de dados do metabase com o banco de dados do projeto (faça isso apenas após executar o `main.py`)

3. Crie as queries necessárias para o projeto e adicione no dashboard como desejar.

### Criando banco e metabase através de docker-compose

- Caso opte por executar através de um docker, basta executar o comando `docker-compose up -d` na raiz do projeto e copiar o arquivo `.env.example` para `.env`. As variaveis de conexão já estão configuradas.

- O arquivo `docker-compose.yml` irá criar 3 containers
  - 1 com um banco de dados postgres que servirá para armazenar os dados do metabase
  - 1 com 1 banco de dados postgres que servirá para armazenar os dados para analise
  - 1 com o metabase

## Descrição do projeto

O projeto consiste em estudar ETL (Extract, Transform, Load) e Data Warehouse. Para isso, foi escolhido um dataset do Kaggle que contém informações sobre obesidade. O dataset foi escolhido por conter informações relevantes para a análise de dados e por ser um tema de saúde pública.

Foram feitos jobs(scripts) para extrair os dados do dataset, transformar e carregar em um banco de dados PostgreSQL. Além disso, foi feita a modelagem de um Data Warehouse, assim como dimensões e fatos e a criação de um dashboard no Metabase.

## Dimensões escolhidas

1. **Demografia**:
   - Variáveis: `gender`, `age`, `family_history_with_overweight`
   - Justificativa: Essas variáveis ajudam a entender a relação entre características demográficas e níveis de obesidade.

2. **Comportamento Alimentar**:
   - Variáveis: `favc`, `fcvc`
   - Justificativa: Compreender os hábitos alimentares pode revelar padrões que contribuem para a obesidade.

3. **Atividade Física**:
   - Variáveis: `faf`, `ch2o`
   - Justificativa: A atividade física é um fator importante na prevenção da obesidade e sua análise pode ajudar a identificar áreas de intervenção.

4. **Estilo de Vida**:
   - Variáveis: `smoke`, `calc`, `mtrans`
   - Justificativa: O estilo de vida pode impactar significativamente a saúde, e analisar essas variáveis pode fornecer insights valiosos.

## Fato

- **Obesidade**:
  - Colunas: `id`, `weight`, `height`, `demografia_id`, `comportamento_alimentar_id`, `atividade_fisica_id`, `estilo_de_vida_id`
- **Hábito Alimentar**:
  - Colunas: `id`, `ncp`, `comportamento_alimentar_id` (Falta implementar)
