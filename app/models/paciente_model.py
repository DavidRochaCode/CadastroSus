from models.database import Database
import logging

class PacienteModel:
    def __init__(self, db: Database):
        self.db = db

    def criar_tabela(self):
        logging.info("Criando tabela de pacientes, se não existir.")
        query = """
        CREATE TABLE IF NOT EXISTS paciente (
            nome VARCHAR(100),
            sobrenome VARCHAR(100),
            cpf_paciente VARCHAR(11) PRIMARY KEY,
            cartao_sus VARCHAR(15),
            endereco VARCHAR(255),
            celular VARCHAR(15),
            prontuario INT
        );
        """
        try:
            self.db.execute(query)
            logging.info("Tabela de pacientes criada com sucesso.")
        except Exception as e:
            logging.error("Erro ao criar tabela de pacientes: %s", e)
            raise

    def inserir_paciente(self, nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario):
        logging.info("Inserindo paciente com CPF: %s", cpf)
        query = """
        INSERT INTO paciente (nome, sobrenome, cpf_paciente, cartao_sus, endereco, celular, prontuario)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (cpf_paciente) DO NOTHING;
        """
        try:
            self.db.execute(query, (nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario))
            logging.info("Paciente inserido com sucesso.")
        except Exception as e:
            logging.error("Erro ao inserir paciente: %s", e)
            raise

    def atualizar_paciente(self, nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario):
        logging.info("Atualizando paciente com CPF: %s", cpf)
        query = """
        UPDATE paciente
        SET nome = %s, sobrenome = %s, cartao_sus = %s, endereco = %s, celular = %s, prontuario = %s
        WHERE cpf_paciente = %s;
        """
        try:
            self.db.execute(query, (nome, sobrenome, cartao_sus, endereco, celular, prontuario, cpf))
            logging.info("Paciente atualizado com sucesso.")
        except Exception as e:
            logging.error("Erro ao atualizar paciente: %s", e)
            raise

    def buscar_paciente_por_cpf(self, cpf):
        logging.info("Buscando paciente com CPF: %s", cpf)
        query = "SELECT * FROM paciente WHERE cpf_paciente = %s;"
        try:
            paciente = self.db.fetch_all(query, (cpf,))
            logging.info("Paciente encontrado: %s", paciente)
            return paciente
        except Exception as e:
            logging.error("Erro ao buscar paciente: %s", e)
            raise
