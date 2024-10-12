from jobs.download_dataset import download_dataset
from jobs.insert_data_on_db import create_table_on_db, insert_data_from_csv
from jobs.normalizing_data import NormalizingData

if __name__ == "__main__":
    try:
        download_dataset()
        create_table_on_db("infra/configs/create_table.sql")
        insert_data_from_csv("data/ObesityDataSet_raw_and_data_sinthetic.csv")
        normalizing = NormalizingData()
        # Cria as tabelas de dimensão
        normalizing.create_dimension_demografia()
        normalizing.create_dimension_compalimentar()
        normalizing.create_dimension_atividade_fisica()
        normalizing.create_dimension_estilo_vida()
        # Cria a tabela de fato
        normalizing.create_fact_obesidade()
    except Exception as e:
        print(f"Erro ao executar o job: {e}")