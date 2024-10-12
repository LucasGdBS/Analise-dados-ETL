import sys,os
sys.path.insert(0,os.path.abspath(os.curdir))

from infra.configs.db_connection_handler import DBConnectionHandler

class NormalizingData:
    def create_dimension_demografia(self):
        # Cria a tabela no banco
        with DBConnectionHandler() as db:
            try:
                db.cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS demografia (
                        id SERIAL PRIMARY KEY,
                        gender VARCHAR(10),
                        age INTEGER,
                        family_history_with_overweight BOOLEAN,
                        UNIQUE (gender, age)
                    );
                    """
                )
                print("Tabela demografia criada com sucesso!")
            except Exception as e:
                print(f"Erro ao criar tabela: {e}")
                db.conn.rollback()
                return
        
        with DBConnectionHandler() as db:
            try:               
                db.cur.execute(
                    """
                    INSERT INTO demografia (gender, age, family_history_with_overweight)
                    SELECT DISTINCT gender, age,
                        CASE
                            WHEN family_history_with_overweight = 'yes' THEN TRUE
                            WHEN family_history_with_overweight = 'no' THEN FALSE
                        END
                    FROM data_raw
                    ON CONFLICT (gender, age) DO NOTHING
                    """
                )
                print("Dados inseridos com sucesso!")
            except Exception as e:
                print(f"Erro ao inserir dados: {e}")
                db.conn.rollback()
                return
    
    def create_dimension_compalimentar(self):
        with DBConnectionHandler() as db:
            try:
                db.cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS compalimentar (
                        id SERIAL PRIMARY KEY,
                        favc BOOLEAN,
                        fcvc INTEGER,
                        UNIQUE (favc, fcvc)
                    );
                    """
                )
                print("Tabela compalimentar criada com sucesso!")
            except Exception as e:
                print(f"Erro ao criar tabela: {e}")
                db.conn.rollback()
                return
        
        with DBConnectionHandler() as db:
            try:               
                db.cur.execute(
                    """
                    INSERT INTO compalimentar (fcvc, favc)
                    SELECT DISTINCT fcvc,
                        CASE
                            WHEN favc = 'yes' THEN TRUE
                            WHEN favc = 'no' THEN FALSE
                        END
                    FROM data_raw
                    ON CONFLICT (favc, fcvc) DO NOTHING
                    """
                )
                print("Dados inseridos com sucesso!")
            except Exception as e:
                print(f"Erro ao inserir dados: {e}")
                db.conn.rollback()
                return

    def create_dimension_atividade_fisica(self):
        # Criar a tabela no banco
        with DBConnectionHandler() as db:
            try:
                db.cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS atividade_fisica (
                        id SERIAL PRIMARY KEY,
                        faf INTEGER,
                        ch2o FLOAT,
                        UNIQUE (faf, ch2o)
                    );
                    """
                )
                print("Tabela atividade_fisica criada com sucesso!")
            except Exception as e:
                print(f"Erro ao criar tabela: {e}")
                db.conn.rollback()
                return
        
        with DBConnectionHandler() as db:
            try:               
                db.cur.execute(
                    """
                    INSERT INTO atividade_fisica (faf, ch2o)
                    SELECT DISTINCT faf, ch2o
                    FROM data_raw
                    ON CONFLICT (faf, ch2o) DO NOTHING
                    """
                )
                print("Dados inseridos com sucesso!")
            except Exception as e:
                print(f"Erro ao inserir dados: {e}")
                db.conn.rollback()
                return

    def create_dimension_estilo_vida(self):
        # Criar a tabela no banco
        with DBConnectionHandler() as db:
            try:
                db.cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS estilo_vida (
                        id SERIAL PRIMARY KEY,
                        smoke BOOLEAN,
                        calc VARCHAR(50),
                        mtrans VARCHAR(50),
                        UNIQUE (smoke, calc, mtrans)
                    );
                    """
                )
                print("Tabela estilo_vida criada com sucesso!")
            except Exception as e:
                print(f"Erro ao criar tabela: {e}")
                db.conn.rollback()
                return
        
        with DBConnectionHandler() as db:
            try:               
                db.cur.execute(
                    """
                    INSERT INTO estilo_vida (smoke, calc, mtrans)
                    SELECT DISTINCT 
                        CASE
                            WHEN smoke = 'yes' THEN TRUE
                            WHEN smoke = 'no' THEN FALSE
                        END AS smoke,
                        calc,
                        mtrans
                    FROM data_raw
                    ON CONFLICT (smoke, calc, mtrans) DO NOTHING
                    """
                )
                print("Dados inseridos com sucesso!")
            except Exception as e:
                print(f"Erro ao inserir dados: {e}")
                db.conn.rollback()
                return
    
    def create_fact_obesidade(self):
        # Criar a tabela no banco
        with DBConnectionHandler() as db:
            try:
                db.cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS obesidade (
                        id SERIAL PRIMARY KEY,
                        weight FLOAT,
                        height FLOAT,
                        demografia_id INTEGER REFERENCES demografia(id),
                        comportamento_alimentar_id INTEGER REFERENCES compalimentar(id),
                        atividade_fisica_id INTEGER REFERENCES atividade_fisica(id),
                        estilo_de_vida_id INTEGER REFERENCES estilo_vida(id),
                        nobeyesdad VARCHAR(50) NOT NULL
                    );
                    """
                )
                print("Tabela obesidade criada com sucesso!")
            except Exception as e:
                print(f"Erro ao criar tabela: {e}")
                db.conn.rollback()
                return
        
        with DBConnectionHandler() as db:
            try:               
                db.cur.execute(
                    """
                    INSERT INTO obesidade (weight, height, demografia_id, comportamento_alimentar_id, atividade_fisica_id, estilo_de_vida_id, nobeyesdad)
                    SELECT
                        r.weight,
                        r.height,
                        d.id AS demografia_id,
                        c.id AS comportamento_alimentar_id,
                        a.id AS atividade_fisica_id,
                        e.id AS estilo_de_vida_id,
                        r.nobeyesdad
                    FROM
                        data_raw r
                    LEFT JOIN demografia d
                        ON r.gender = d.gender
                        AND r.age = d.age
                        AND CASE 
                            WHEN r.family_history_with_overweight = 'yes' THEN TRUE
                            WHEN r.family_history_with_overweight = 'no' THEN FALSE
                            ELSE NULL
                        END = d.family_history_with_overweight
                    LEFT JOIN compalimentar c
                        ON CASE
                            WHEN r.favc = 'yes' THEN TRUE
                            WHEN r.favc = 'no' THEN FALSE
                        END = c.favc
                        AND r.fcvc = c.fcvc
                    LEFT JOIN atividade_fisica a
                        ON r.faf = a.faf
                        AND r.ch2o = a.ch2o
                    LEFT JOIN estilo_vida e
                        ON CASE
                            WHEN r.smoke = 'yes' THEN TRUE
                            WHEN r.smoke = 'no' THEN FALSE
                        END = e.smoke
                        AND r.calc = e.calc
                        AND r.mtrans = e.mtrans
                    ON CONFLICT DO NOTHING;
                    """
                )
                print("Dados inseridos com sucesso na tabela obesidade!")
            except Exception as e:
                print(f"Erro ao inserir dados na tabela obesidade: {e}")
                db.conn.rollback()
                return
        

if __name__ == "__main__":
    # Criando as dimensões para o fato de obesidade

    NormalizingData().create_dimension_demografia()
    NormalizingData().create_dimension_compalimentar()
    NormalizingData().create_dimension_atividade_fisica()
    NormalizingData().create_dimension_estilo_vida()

    # Criando o fato de obesidade
    NormalizingData().create_fact_obesidade()
        
        