import logging
from app.database.database_interface import DatabaseInterface  # Importa a interface do banco de dados

class PacienteModel:
    def __init__(self, db: DatabaseInterface):
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
            prontuario INT,
            status VARCHAR(100)
        );
        """
        try:
            self.db.execute(query)
            logging.info("Tabela de pacientes criada com sucesso.")
        except Exception as e:
            logging.error("Erro ao criar tabela de pacientes: %s", e)
            raise

    def inserir_paciente(self, nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario, status = 'ativo'):
        logging.info("Inserindo paciente com CPF: %s", cpf)
        if self.verificar_paciente_existe(cpf):
            logging.warning("Paciente com CPF %s já existe. Atualização abortada.", cpf)
            return True  # Paciente não encontrado
        query = """
        INSERT INTO paciente (nome, sobrenome, cpf_paciente, cartao_sus, endereco, celular, prontuario, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (cpf_paciente) DO NOTHING;
        """
        try:
            self.db.execute(query, (nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario, status))
            logging.info("Paciente inserido com sucesso.")
            return False
        except Exception as e:
            logging.error("Erro ao inserir paciente: %s", e)
            raise

    def verificar_paciente_existe(self, cpf):
        """
        Verifica se um paciente com o CPF especificado existe.
        """
        logging.info("Verificando se o paciente com CPF %s existe.", cpf)
        query = "SELECT COUNT(*) FROM paciente WHERE cpf_paciente = %s;"
        try:
            resultado = self.db.fetch_all(query, (cpf,))
            return resultado[0][0] > 0  # Retorna True se o paciente existir
        except Exception as e:
            logging.error("Erro ao verificar paciente: %s", e)
            raise
        
    def atualizar_paciente(self, nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario, status):
        logging.info("Atualizando paciente com CPF: %s", cpf)
        # Verifica se o paciente existe
        if not self.verificar_paciente_existe(cpf):
            logging.warning("Paciente com CPF %s não encontrado. Atualização abortada.", cpf)
            return False  # Paciente não encontrado
        query = """
        UPDATE paciente
        SET nome = %s, sobrenome = %s, cartao_sus = %s, endereco = %s, celular = %s, prontuario = %s, status = %s
        WHERE cpf_paciente = %s;
        """
        try:
            self.db.execute(query, (nome, sobrenome, cartao_sus, endereco, celular, prontuario, status, cpf))
            logging.info("Paciente atualizado com sucesso.")
            return True
        except Exception as e:
            logging.error("Erro ao atualizar paciente: %s", e)
            raise

    def buscar_paciente_por_cpf(self, cpf):
        logging.info("Buscando paciente com CPF: %s", cpf)
        if not self.verificar_paciente_existe(cpf):
            logging.warning("Paciente com CPF %s não encontrado.", cpf)
            return False  # Paciente não encontrado
        
        query = """
            SELECT nome, sobrenome, cpf_paciente, cartao_sus, endereco, celular, prontuario, status
            FROM paciente
            WHERE cpf_paciente = %s;
        """
        try:
            pacientes = self.db.fetch_all(query, (cpf,))  # Busca os pacientes
            if not pacientes:
                return False
            
            paciente = pacientes[0]  # Seleciona o primeiro registro
            # Mapeando o registro para um dicionário
            paciente_dict = {
                "nome": paciente[0],
                "sobrenome": paciente[1],
                "cpf_paciente": paciente[2],
                "cartao_sus": paciente[3],
                "endereco": paciente[4],
                "celular": paciente[5],
                "prontuario": paciente[6],
                "status": paciente[7],
            }
            logging.info("Paciente encontrado: %s", paciente_dict)
            return paciente_dict  # Retorna o dicionário com os campos do paciente
        except Exception as e:
            logging.error("Erro ao buscar paciente: %s", e)
            raise


    def deletar_paciente(self, cpf):
        logging.info("Deletando paciente com CPF: %s", cpf)
        # Verifica se o paciente existe
        if not self.verificar_paciente_existe(cpf):
            logging.warning("Paciente com CPF %s não encontrado. Atualização abortada.", cpf)
            return False  # Paciente não encontrado
        query = "DELETE FROM paciente WHERE cpf_paciente = %s;"
        try:
            self.db.execute(query, (cpf,))
            logging.info("Paciente deletado com sucesso.")
            return True
        except Exception as e:
            logging.error("Erro ao deletar paciente: %s", e)
            raise
