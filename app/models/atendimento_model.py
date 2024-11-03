from models.database import Database
import logging

class AtendimentoModel:
    def __init__(self, db: Database):
        self.db = db

    def criar_tabela(self):
        logging.info("Criando tabela de atendimentos, se não existir.")
        query = """
        CREATE TABLE IF NOT EXISTS atendimento (
            cod_atendimento SERIAL PRIMARY KEY,
            cpf_paciente VARCHAR(11) REFERENCES paciente(cpf_paciente),
            crm INT REFERENCES medico(crm),
            data_atendimento DATE DEFAULT CURRENT_DATE
        );
        """
        try:
            self.db.execute(query)
            logging.info("Tabela de atendimentos criada com sucesso.")
        except Exception as e:
            logging.error("Erro ao criar tabela de atendimentos: %s", e)
            raise

    def inserir_atendimento(self, cod_atendimento, cpf_paciente, crm):
        logging.info("Inserindo registro de atendimento.")
        query = """
        INSERT INTO atendimento (cod_atendimento, cpf_paciente, crm)
        VALUES (%s, %s, %s);
        """
        try:
            self.db.execute(query, (cod_atendimento, cpf_paciente, crm))
            logging.info("Registro de atendimento inserido com sucesso.")
        except Exception as e:
            logging.error("Erro ao inserir atendimento: %s", e)
            raise

    def buscar_atendimento_por_codigo(self, cod_atendimento):
        logging.info("Buscando atendimento pelo código: %s", cod_atendimento)
        query = """
        SELECT * FROM atendimento
        WHERE cod_atendimento = %s;
        """
        try:
            atendimento = self.db.fetch_all(query, (cod_atendimento,))
            logging.info("Atendimento encontrado: %s", atendimento)
            return atendimento
        except Exception as e:
            logging.error("Erro ao buscar atendimento: %s", e)
            raise

    def deletar_atendimento(self, cod_atendimento):
        logging.info("Deletando atendimento com código: %s", cod_atendimento)
        query = """
        DELETE FROM atendimento
        WHERE cod_atendimento = %s;
        """
        try:
            self.db.execute(query, (cod_atendimento,))
            logging.info("Atendimento deletado com sucesso.")
        except Exception as e:
            logging.error("Erro ao deletar atendimento: %s", e)
            raise
