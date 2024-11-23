import logging
from app.database.database_interface import DatabaseInterface  # Importa a interface do banco de dados

class AtendenteModel:
    def __init__(self, db: DatabaseInterface):
        self.db = db

    def criar_tabela(self):
        logging.info("Criando tabela de atendentes, se não existir.")
        query = """
        CREATE TABLE IF NOT EXISTS atendente (
            nome VARCHAR(100),
            sobrenome VARCHAR(100),
            cod_atendente SERIAL PRIMARY KEY
        );
        """
        try:
            self.db.execute(query)
            logging.info("Tabela de atendentes criada ou já existente.")
        except Exception as e:
            logging.error("Erro ao criar tabela de atendentes: %s", e)
            raise
        
    def inserir_atendente(self, nome, sobrenome, cod_atendente):
        logging.info("Inserindo atendente: %s %s, Código: %s", nome, sobrenome, cod_atendente)
        
        if self.verificar_atendente_existe(cod_atendente):
            logging.warning("Atendente com código %s Já existe. Operação abortada.", cod_atendente)
            return True 
        
        query = """
        INSERT INTO atendente (nome, sobrenome, cod_atendente)
        VALUES (%s, %s, %s)
        """
        try:
            self.db.execute(query, (nome, sobrenome, cod_atendente))
            logging.info("Atendente inserido com sucesso.")
            return False
        except Exception as e:
            logging.error("Erro ao inserir atendente: %s", e)
            raise

    def verificar_atendente_existe(self, cod_atendente):
        """
        Verifica se um atendente com o código especificado existe.
        """
        logging.info("Verificando se o atendente com código %s existe.", cod_atendente)
        query = "SELECT COUNT(*) FROM atendente WHERE cod_atendente = %s;"
        try:
            resultado = self.db.fetch_all(query, (cod_atendente,))
            return resultado[0][0] > 0
                
        except Exception as e:
            logging.error("Erro ao verificar atendente: %s", e)
            raise

    def atualizar_atendente(self, nome, sobrenome, cod_atendente):
        logging.info("Atualizando atendente com controle %s.", cod_atendente)

        # Verifica se o atendente existe
        if not self.verificar_atendente_existe(cod_atendente):
            logging.warning("Atendente com código %s não encontrado. Atualização abortada.", cod_atendente)
            return False  # Retorna False se o atendente não for encontrado

        query = """
        UPDATE atendente
        SET nome = %s, sobrenome = %s
        WHERE cod_atendente = %s;
        """
        try:
            self.db.execute(query, (nome, sobrenome, cod_atendente))
            logging.info("Atendente atualizado com sucesso.")
            return True
        except Exception as e:
            logging.error("Erro ao atualizar atendente: %s", e)
            raise

    def buscar_atendentes(self):
        logging.info("Buscando todos os registros de atendentes.")
        try:
            registros = self.db.fetch_all("SELECT * FROM atendente")
            logging.info("Registros de atendentes recuperados com sucesso.")
            atendentes = [
                {
                    'nome': registro[0],
                    'sobrenome': registro[1],
                    'cod_atendente': registro[2],
                }
                for registro in registros
            ]
            return atendentes
        except Exception as e:
            logging.error("Erro ao buscar atendentes: %s", e)
            raise


    def deletar_atendente(self, cod_atendente):
        logging.info("Deletando atendente com controle: %s", cod_atendente)

        # Verifica se o atendente existe
        if not self.verificar_atendente_existe(cod_atendente):
            logging.warning("Atendente com código %s não encontrado. Exclusão abortada.", cod_atendente)
            return False  # Retorna False se o atendente não for encontrado

        query = "DELETE FROM atendente WHERE cod_atendente = %s;"
        try:
            self.db.execute(query, (cod_atendente,))
            logging.info("Atendente deletado com sucesso.")
            return True
        except Exception as e:
            logging.error("Erro ao deletar atendente: %s", e)
            raise
