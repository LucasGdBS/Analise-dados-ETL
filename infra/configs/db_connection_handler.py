import psycopg2
from decouple import config as env

class DBConnectionHandler:
    def __init__(self):
        self.conn = self.__create_database_engine()
        self.cur = self.conn.cursor()  # Use self.conn para criar o cursor

    def __create_database_engine(self):
        '''Método usado para criar a conexão do nosso código com o banco'''
        conn = psycopg2.connect(
            dbname=env("DB_NAMED"),
            user=env("DB_USER"),
            password=env("DB_PASSWORD"),
            host=env("DB_HOST"),
            port=env("DB_PORT")
        )
        return conn
    
    def get_conn(self):
        '''Método para retornar a conexão com o banco'''
        return self.conn

    def __enter__(self):
        '''Método mágico que é executado ao entrar em um bloco with'''
        return self # Retorna a instância da própria classe

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''Método mágico que é executado ao sair de um bloco with'''
        self.conn.commit() # Faça o commit antes de fechar a conex
        self.cur.close()  # Feche o cursor antes de fechar a conexão
        self.conn.close()  # Feche a conexão com o banco de dados

    