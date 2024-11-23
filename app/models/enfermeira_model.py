import logging
from app.database.database_interface import DatabaseInterface  # Importa a interface do banco de dados

class EnfermeiraModel:
    def __init__(self, db: DatabaseInterface):
        self.db = db

    def criar_tabela(self):
        logging.info("Criando tabela de enfermeiras, se não existir.")
        query = """
        CREATE TABLE IF NOT EXISTS enfermeira (
            codigo SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            setor VARCHAR(100) NOT NULL
        );
        """
        try:
            self.db.execute(query)
            logging.info("Tabela de enfermeiras criada com sucesso.")
        except Exception as e:
            logging.error("Erro ao criar tabela de enfermeiras: %s", e)
            raise

    def inserir_enfermeira(self, nome, setor):
        logging.info("Inserindo enfermeira: %s, Setor: %s", nome, setor)
        query = """
        INSERT INTO enfermeira (nome, setor)
        VALUES (%s, %s);
        """
        try:
            self.db.execute(query, (nome, setor))
            logging.info("Enfermeira inserida com sucesso.")
        except Exception as e:
            logging.error("Erro ao inserir enfermeira: %s", e)
            raise

    def buscar_todas_enfermeiras(self):
        logging.info("Buscando todas as enfermeiras.")
        query = "SELECT codigo, nome, setor FROM enfermeira;"
        try:
            registros = self.db.fetch_all(query)
            enfermeiras = [{"codigo": registro[0], "nome": registro[1], "setor": registro[2]} for registro in registros]
            logging.info("Enfermeiras encontradas: %s", enfermeiras)
            return enfermeiras
        except Exception as e:
            logging.error("Erro ao buscar enfermeiras: %s", e)
            raise

    def verificar_enfermeira_existe(self, codigo):
        logging.info("Verificando se a enfermeira com código %s existe.", codigo)
        query = "SELECT COUNT(*) FROM enfermeira WHERE codigo = %s;"
        try:
            resultado = self.db.fetch_all(query, (codigo,))
            return resultado[0][0] > 0
        except Exception as e:
            logging.error("Erro ao verificar enfermeira: %s", e)
            raise

    def atualizar_enfermeira(self, codigo, nome, setor):
        logging.info("Atualizando enfermeira com código %s: Nome = %s, Setor = %s", codigo, nome, setor)

        if not self.verificar_enfermeira_existe(codigo):
            logging.warning("Enfermeira com código %s não encontrada. Operação abortada.", codigo)
            return False  # Enfermeira não encontrada

        query = """
        UPDATE enfermeira
        SET nome = %s, setor = %s
        WHERE codigo = %s;
        """
        try:
            self.db.execute(query, (nome, setor, codigo))
            logging.info("Enfermeira atualizada com sucesso.")
            return True
        except Exception as e:
            logging.error("Erro ao atualizar enfermeira: %s", e)
            raise

    def deletar_enfermeira(self, codigo):
        logging.info("Deletando enfermeira com código: %s", codigo)
        
        if not self.verificar_enfermeira_existe(codigo):
            logging.warning("Enfermeira com código %s não encontrada. Operação abortada.", codigo)
            return False  # Enfermeira não encontrada
        query = "DELETE FROM enfermeira WHERE codigo = %s;"
        try:
            self.db.execute(query, (codigo,))
            logging.info("Enfermeira deletada com sucesso.")
            return True
        except Exception as e:
            logging.error("Erro ao deletar enfermeira: %s", e)
            raise
