import logging
from app.database.database_interface import DatabaseInterface  # Importa a interface do banco de dados

class AtendimentoModel:
    def __init__(self, db: DatabaseInterface):
        self.db = db

    def criar_tabela(self):
        logging.info("Criando tabela de atendimentos, se não existir.")
        query_medico = """
        select crm from medico
        """
        try:
            self.db.execute(query_medico)
            logging.info("Tabela de atendimentos criada com sucesso.")
        except Exception as e:
            logging.error("Erro ao criar tabela de atendimentos: %s", e)
            raise
        
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
        logging.info("Tentando inserir um registro de atendimento.")

        # Verificar se o CRM existe na tabela 'medico'
        verificar_crm_query = "SELECT COUNT(*) FROM medico WHERE crm = %s;"
        try:
            resultado_crm = self.db.fetch_all(verificar_crm_query, (crm,))
            if resultado_crm[0][0] == 0:  # Nenhum registro encontrado
                logging.warning("CRM %s não encontrado. Abortando a operação.", crm)
                return -1  # Código indicando CRM não encontrado
        except Exception as e:
            logging.error("Erro ao verificar a existência do CRM: %s", e)
            raise

        # Verificar se o CPF do paciente existe na tabela 'paciente'
        verificar_cpf_query = "SELECT COUNT(*) FROM paciente WHERE cpf_paciente = %s;"
        try:
            resultado_cpf = self.db.fetch_all(verificar_cpf_query, (cpf_paciente,))
            if resultado_cpf[0][0] == 0:  # Nenhum registro encontrado
                logging.warning("CPF do paciente %s não encontrado. Abortando a operação.", cpf_paciente)
                return -2  # Código indicando CPF do paciente não encontrado
        except Exception as e:
            logging.error("Erro ao verificar a existência do CPF do paciente: %s", e)
            raise

        # Inserir o atendimento se o CRM e o CPF forem válidos
        query = """
        INSERT INTO atendimento (cod_atendimento, cpf_paciente, crm)
        VALUES (%s, %s, %s);
        """
        try:
            self.db.execute(query, (cod_atendimento, cpf_paciente, crm))
            logging.info("Registro de atendimento inserido com sucesso.")
            return 1  # Código indicando sucesso
        except Exception as e:
            logging.error("Erro ao inserir atendimento: %s", e)
            raise



    def buscar_atendimento_por_codigo(self, cod_atendimento: int):
        logging.info("Buscando atendimento pelo código: %s", cod_atendimento)

        # Verificar se o atendimento existe
        verificar_cod_query = "SELECT COUNT(*) FROM atendimento WHERE cod_atendimento = %s;"
        try:
            resultado_cod = self.db.fetch_all(verificar_cod_query, (cod_atendimento,))
            if resultado_cod[0][0] == 0:  # Nenhum registro encontrado
                logging.warning("Cod %s não encontrado. Abortando a operação.", cod_atendimento)
                return -1  # Código indicando atendimento não encontrado
        except Exception as e:
            logging.error("Erro ao verificar a existência do cod_atendimento: %s", e)
            raise

        # Buscar o atendimento com detalhes
        query = """
        SELECT
            A.COD_ATENDIMENTO AS CODIGO,
            A.DATA_ATENDIMENTO,
            P.NOME AS NOME_PACIENTE,
            P.SOBRENOME,
            P.CELULAR,
            P.PRONTUARIO,
            P.CARTAO_SUS,
            P.CPF_PACIENTE,
            M.NOME AS NOME_MEDICO,
            M.ATUACAO,
            M.CRM
        FROM
            ATENDIMENTO A
            LEFT JOIN PACIENTE P ON A.CPF_PACIENTE = P.CPF_PACIENTE
            LEFT JOIN MEDICO M ON A.CRM = M.CRM
        WHERE A.COD_ATENDIMENTO = %s;
        """
        try:
            atendimento = self.db.fetch_all(query, (cod_atendimento,))
            if atendimento:
                # Processar o atendimento para retornar como dicionário
                resultado = {
                    "codigo": atendimento[0][0],
                    "data_atendimento": atendimento[0][1],
                    "nome_paciente": atendimento[0][2],
                    "sobrenome_paciente": atendimento[0][3],
                    "celular": atendimento[0][4],
                    "prontuario": atendimento[0][5],
                    "cartao_sus": atendimento[0][6],
                    "cpf_paciente": atendimento[0][7],
                    "nome_medico": atendimento[0][8],
                    "atuacao_medico": atendimento[0][9],
                    "crm_medico": atendimento[0][10],
                }
                logging.info("Atendimento encontrado: %s", resultado)
                return resultado
            return -1  # Caso não encontre, por precaução
        except Exception as e:
            logging.error("Erro ao buscar atendimento: %s", e)
            raise


    def deletar_atendimento(self, cod_atendimento):
        logging.info("Deletando atendimento com código: %s", cod_atendimento)
        
        
        verificar_cod_query = "SELECT COUNT(*) FROM atendimento WHERE cod_atendimento = %s;"
        try:
            resultado_cod = self.db.fetch_all(verificar_cod_query, (cod_atendimento,))
            if resultado_cod[0][0] == 0:  # Nenhum registro encontrado
                logging.warning("Cod %s não encontrado. Abortando a operação.", cod_atendimento)
                return -1  # Código indicando cod não encontrado
        except Exception as e:
            logging.error("Erro ao verificar a existência do Cod_atendimento: %s", e)
            raise
        
        query = "DELETE FROM atendimento WHERE cod_atendimento = %s;"
        try:
            self.db.execute(query, (cod_atendimento,))
            logging.info("Atendimento deletado com sucesso.")
        except Exception as e:
            logging.error("Erro ao deletar atendimento: %s", e)
            raise
