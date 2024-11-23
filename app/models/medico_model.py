import logging
from app.database.database_interface import DatabaseInterface  # Importa a interface do banco de dados

class MedicoModel:
    def __init__(self, db: DatabaseInterface):
        self.db = db

    def criar_tabela(self):
        logging.info("Criando tabela de médicos, se não existir.")
        query = """
        CREATE TABLE IF NOT EXISTS medico (
            crm INT PRIMARY KEY,
            nome VARCHAR(100),
            atuacao VARCHAR(100)
        );
        """
        try:
            self.db.execute(query)
            logging.info("Tabela de médicos criada com sucesso.")
        except Exception as e:
            logging.error("Erro ao criar tabela de médicos: %s", e)
            raise

    def inserir_medico(self, crm, nome, atuacao):
        logging.info("Inserindo médico com CRM: %s", crm)
        if self.verificar_medico_existe(crm):
            logging.warning("Médico com CRM %s já existe. operação abortada.", crm)
            return True  # Médico encontrado
        query = """
        INSERT INTO medico (crm, nome, atuacao)
        VALUES (%s, %s, %s)
        ON CONFLICT (crm) DO UPDATE SET nome = EXCLUDED.nome, atuacao = EXCLUDED.atuacao;
        """
        try:
            self.db.execute(query, (crm, nome, atuacao))
            logging.info("Médico inserido ou atualizado com sucesso.")
            return False
        except Exception as e:
            logging.error("Erro ao inserir médico: %s", e)
            raise
    def verificar_medico_existe(self, crm):
        """
        Verifica se um médico com o CRM especificado existe.
        """
        logging.info("Verificando se o médico com CRM %s existe.", crm)
        query = "SELECT COUNT(*) FROM medico WHERE crm = %s;"
        try:
            resultado = self.db.fetch_all(query, (crm,))
            return resultado[0][0] > 0  # Retorna True se o médico existir
        except Exception as e:
            logging.error("Erro ao verificar médico: %s", e)
            raise

    def atualizar_medico(self, crm, nome, atuacao):
        logging.info("Atualizando médico com CRM: %s", crm)
         # Verifica se o médico existe
        if not self.verificar_medico_existe(crm):
            logging.warning("Médico com CRM %s não encontrado. Atualização abortada.", crm)
            return False  # Médico não encontrado
        query = """
        UPDATE medico
        SET nome = %s, atuacao = %s
        WHERE crm = %s;
        """
        try:
            self.db.execute(query, (nome, atuacao, crm))
            logging.info("Médico atualizado com sucesso.")
            return True
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
        
    def buscar_todos_medicos(self):
        logging.info("Buscando todos os médicos.")
        query = """
        SELECT crm, nome, atuacao
        FROM medico;
        """
        try:
            medicos = self.db.fetch_all(query)
            logging.info("Médicos encontrados: %s", medicos)
            return [
                {"crm": medico[0], "nome": medico[1], "atuacao": medico[2]}
                for medico in medicos
            ]
        except Exception as e:
            logging.error("Erro ao buscar médicos: %s", e)
            raise
        

    def deletar_medico(self, crm):
        logging.info("Deletando médico com CRM: %s", crm)
         # Verifica se o médico existe
        if not self.verificar_medico_existe(crm):
            logging.warning("Médico com CRM %s não encontrado. Atualização abortada.", crm)
            return False  # Médico não encontrado
        query = "DELETE FROM medico WHERE crm = %s;"
        try:
            self.db.execute(query, (crm,))
            logging.info("Médico deletado com sucesso.")
            return True
        except Exception as e:
            logging.error("Erro ao deletar médico: %s", e)
            raise
