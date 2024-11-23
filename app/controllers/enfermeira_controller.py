import logging
from app.models.enfermeira_model import EnfermeiraModel

class EnfermeiraController:
    def __init__(self, enfermeira_model: EnfermeiraModel):
        self.enfermeira_model = enfermeira_model

    def inserir_enfermeira(self, nome, setor):
        logging.info("Inserindo enfermeira: Nome = %s, Setor = %s", nome, setor)
        try:
            self.enfermeira_model.inserir_enfermeira(nome, setor)
            logging.info("Enfermeira inserida com sucesso.")
        except Exception as e:
            logging.error("Erro ao inserir enfermeira: %s", e)
            raise

    def buscar_todas_enfermeiras(self):
        logging.info("Buscando todas as enfermeiras.")
        try:
            enfermeiras = self.enfermeira_model.buscar_todas_enfermeiras()
            logging.info("Enfermeiras encontradas: %s", enfermeiras)
            return enfermeiras
        except Exception as e:
            logging.error("Erro ao buscar enfermeiras: %s", e)
            raise

    def atualizar_enfermeira(self, codigo, nome, setor):
        logging.info("Atualizando enfermeira com código %s: Nome = %s, Setor = %s", codigo, nome, setor)
        try:
            resultado = self.enfermeira_model.atualizar_enfermeira(codigo, nome, setor)
            if not resultado:
                return {"message": f"Enfermeira com código {codigo} não encontrada.", "status": "error"}
            logging.info("Enfermeira atualizada com sucesso.")
            return {"message": "Enfermeira atualizada com sucesso.", "status": "success"}
        except Exception as e:
            logging.error("Erro ao atualizar enfermeira: %s", e)
            raise

    def deletar_enfermeira(self, codigo):
        logging.info("Deletando enfermeira com código: %s", codigo)
        try:
            resultado = self.enfermeira_model.deletar_enfermeira(codigo)
            if not resultado:
                return {"message": f"Enfermeira com código {codigo} não encontrada.", "status": "error"}
            logging.info("Enfermeira deletada com sucesso.")
            return {"message": f"Enfermeira deletada com sucesso", "status": "success"}
        except Exception as e:
            logging.error("Erro ao deletar enfermeira: %s", e)
            raise
