import os
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

def download_dataset():
    api = KaggleApi()
    api.authenticate()

    # Define o caminho desejado para salvar o dataset
    desired_path = "data"
    url_data_set = 'fatemehmehrparvar/obesity-levels'

    # Baixa o dataset no caminho especificado
    api.dataset_download_files(url_data_set, path=desired_path, unzip=True) # Baixa o dataset

    downloaded_files = os.listdir(desired_path) # Lista os arquivos baixados

    for file in downloaded_files:
        print("Arquivo baixado:", file)

    # Renomeia as colunas do dataset
    try:
        df = pd.read_csv(f'{desired_path}/{file}') # Faz a leitura do dataset
        df.columns = [col.lower().replace(" ", "").replace("(", "_").replace(")", "").replace("/", "_") for col in df.columns] # Renomeia as colunas tirando caracteres especiais e espaços
        # TODO: Limpar os dados antes de fazer a inserção no banco de dados
        # TODO: Tem alguns numeros com mutias casas decimais, arredondar para 2 casas decimais
        
        df.to_csv(f'{desired_path}/{file}', index=False)
        print("Colunas renomeadas com sucesso!")
    except Exception as e:
        print(f"Erro ao renomear as colunas: {e}")
