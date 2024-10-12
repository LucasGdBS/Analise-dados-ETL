<!-- markdownlint-disable MD029 -->
# Desafio

## Fazer download do dataset

1. Instale o kaggle

```bash
pip install kaggle
```

2. Crie sua API key no Kaggle. Isso irá gerar um arquivo Json
   3.Coloque o arquivo chamado kaggle.json em `~/.kaggle/kaggle.json` no Linux, OSX, e outros sistemas operacionais baseados em UNIX, e em `C:\Users\<Windows-usernamekaggle\kaggle.json>\.` no Windows.

3. Execute o job downoad_dataset.py para baixar o dataset

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
  - Colunas: `id`, `ncp`, `comportamento_alimentar_id`
