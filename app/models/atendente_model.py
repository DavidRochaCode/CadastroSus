from models.database import Database
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AtendenteModel:
    def __init__(self, db):
        self.db = db

    def criar_tabela(self):
        logging.info("Criando tabela de atendentes, se não existir.")
        query = """
        CREATE TABLE IF NOT EXISTS atendente (
            nome VARCHAR(100),
            sobrenome VARCHAR(100),
            cod_atendente INT,
            cod_controle SERIAL PRIMARY KEY
        );
        """
        try:
            self.db.execute(query)
            logging.info("Tabela de atendentes criada ou já existente.")
        except Exception as e:
            logging.error("Erro ao criar tabela de atendentes: %s", e)
            raise

    def atualizar_atendente(self, nome, sobrenome, cod_atendente, cod_controle):
        logging.info("Atualizando atendente com controle %s.", cod_controle)
        query = """
        UPDATE atendente
        SET nome = %s, sobrenome = %s, cod_atendente = %s
        WHERE cod_controle = %s;
        """
        try:
            self.db.execute(query, (nome, sobrenome, cod_atendente, cod_controle))
            logging.info("Atendente atualizado com sucesso.")
        except Exception as e:
            logging.error("Erro ao atualizar atendente: %s", e)
            raise

    def buscar_atendentes(self):
        logging.info("Buscando todos os registros de atendentes.")
        try:
            registros = self.db.fetch_all("SELECT * FROM atendente")
            logging.info("Registros de atendentes recuperados com sucesso.")
            
            # Convertendo cada tupla em um dicionário
            atendentes = [
                {
                    'nome': registro[0],
                    'sobrenome': registro[1],
                    'cod_atendente': registro[3],
                    'cod_controle': registro[2]
                }
                for registro in registros
            ]
            return atendentes
        except Exception as e:
            logging.error("Erro ao buscar atendentes: %s", e)
            raise
