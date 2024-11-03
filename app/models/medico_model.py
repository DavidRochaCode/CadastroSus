from models.database import Database
import logging

class MedicoModel:
    def __init__(self, db: Database):
        self.db = db

    def criar_tabela(self):
        logging.info("Criando tabela de médicos, se não existir.")
        query = """
        CREATE TABLE IF NOT EXISTS medico (
            crm INT PRIMARY KEY,
            nome VARCHAR(100),
            atuacao VARCHAR(100),
            cod_controle SERIAL
        );
        """
        try:
            self.db.execute(query)
            logging.info("Tabela de médicos criada com sucesso.")
        except Exception as e:
            logging.error("Erro ao criar tabela de médicos: %s", e)
            raise

    def atualizar_medico(self, crm, nome, atuacao):
        logging.info("Atualizando médico com CRM: %s", crm)
        query = """
        UPDATE medico
        SET nome = %s, atuacao = %s
        WHERE crm = %s;
        """
        try:
            self.db.execute(query, (nome, atuacao, crm))
            logging.info("Médico atualizado com sucesso.")
        except Exception as e:
            logging.error("Erro ao atualizar médico: %s", e)
            raise

    def buscar_medico_por_crm(self, crm):
        logging.info("Buscando médico com CRM: %s", crm)
        query = "SELECT * FROM medico WHERE crm = %s;"
        try:
            medico = self.db.fetch_all(query, (crm,))
            logging.info("Médico encontrado: %s", medico)
            return medico
        except Exception as e:
            logging.error("Erro ao buscar médico: %s", e)
            raise

    def inserir_medico(self, crm, nome, atuacao):
        logging.info("Inserindo médico com CRM: %s", crm)
        query = """
        INSERT INTO medico (crm, nome, atuacao)
        VALUES (%s, %s, %s)
        ON CONFLICT (crm) DO UPDATE SET nome = EXCLUDED.nome, atuacao = EXCLUDED.atuacao;
        """
        try:
            self.db.execute(query, (crm, nome, atuacao))
            logging.info("Médico inserido ou atualizado com sucesso.")
        except Exception as e:
            logging.error("Erro ao inserir médico: %s", e)
            raise
