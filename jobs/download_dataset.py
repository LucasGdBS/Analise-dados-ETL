from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# Define o caminho desejado para salvar o dataset
desired_path = "data"

# Baixa o dataset no caminho especificado
api.dataset_download_files("mattop/nutrition-physical-activity-and-obesity", path=desired_path, unzip=True)

print("Dataset baixado em:", desired_path)
