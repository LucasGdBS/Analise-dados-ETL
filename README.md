<!-- markdownlint-disable MD029 -->

# Desagio

## Fazer download do dataset

1. Instale o kaggle

```bash
pip install kaggle
```

2. Crie sua API key no Kaggle. Isso irá gerar um arquivo Json
   3.Coloque o arquivo chamado kaggle.json em `~/.kaggle/kaggle.json` no Linux, OSX, e outros sistemas operacionais baseados em UNIX, e em `C:\Users\<Windows-usernamekaggle\kaggle.json>\.` no Windows.

```bash
kaggle datasets download -d "mattop/nutrition-physical-activity-and-obesity"
```
