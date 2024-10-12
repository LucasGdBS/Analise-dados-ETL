import sys,os
sys.path.insert(0,os.path.abspath(os.curdir))

from infra.configs.db_connection_handler import DBConnectionHandler
import csv


def create_table_on_db(sql_file):
    with open(sql_file, "r") as file:
        sql = file.read()
    
    with DBConnectionHandler() as db:
        try:
            db.cur.execute(sql)
            print("Tabela criada com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir dados no banco de dados: {e}")
            db.conn.rollback()

def insert_data_from_csv(csv_file_path):
    # Abre o arquivo CSV
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Usa DictReader para ler os dados como um dicionário

        with DBConnectionHandler() as db:
            try:
                # Deleta todas as linhas da tabela antes de inserir novos dados
                db.cur.execute("TRUNCATE TABLE data_raw")

                # Para cada linha no CSV, faça a inserção no banco de dados
                for row in reader:
                    sql = """
                    INSERT INTO data_raw (
                        age, gender, height, weight, calc, favc, fcvc, ncp, scc, smoke, 
                        ch2o, family_history_with_overweight, faf, tue, caec, mtrans, nobeyesdad
                    ) VALUES (
                        %(age)s, %(gender)s, %(height)s, %(weight)s, %(calc)s, %(favc)s, 
                        %(fcvc)s, %(ncp)s, %(scc)s, %(smoke)s, %(ch2o)s, %(family_history_with_overweight)s, 
                        %(faf)s, %(tue)s, %(caec)s, %(mtrans)s, %(nobeyesdad)s
                    )   
                    
                    """

                    db.cur.execute(sql, row)

                print("Dados inseridos com sucesso!")
            except Exception as e:
                print(f"Erro ao inserir dados: {e}")
                db.conn.rollback() 

if __name__ == "__main__":
    create_table_on_db("infra/configs/create_table.sql")
    insert_data_from_csv("data/ObesityDataSet_raw_and_data_sinthetic.csv")