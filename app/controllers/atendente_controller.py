from app.models.atendente_model import AtendenteModel
import logging

class AtendenteController:
    def __init__(self, atendente_model: AtendenteModel):
        self.atendente_model = atendente_model

    def buscar_atendentes(self):
        logging.info("Buscando todos os atendentes.")
        try:
            atendentes = self.atendente_model.buscar_atendentes()
            logging.info("Atendentes encontrados: %s", atendentes)
            return atendentes
        except Exception as e:
            logging.error("Erro ao buscar atendentes: %s", e)
            raise

    def inserir_atendente(self, nome, sobrenome, codigo_atendente):
        logging.info("Inserindo atendente: %s %s, Código: %s", nome, sobrenome, codigo_atendente)
        try:
            resultado = self.atendente_model.inserir_atendente(nome, sobrenome, codigo_atendente)
            if resultado:
                return {"message": f"Atendente com código {codigo_atendente} já existe.", "status": "error"}
            return {"message": "Atendente cadastrado com sucesso.", "status": "success"}
        except Exception as e:
            logging.error("Erro ao inserir atendente: %s", e)
            raise

    def alterar_atendente(self, nome, sobrenome, cod_atendente):
        logging.info("Atualizando atendente com código %s.", cod_atendente)
        try:
            resultado = self.atendente_model.atualizar_atendente(nome, sobrenome, cod_atendente)
            if not resultado:
                return {"message": f"Atendente com código {cod_atendente} não encontrado.", "status": "error"}
            return {"message": "Atendente atualizado com sucesso.", "status": "success"}
        except Exception as e:
            logging.error("Erro ao atualizar atendente: %s", e)
            raise

    def deletar_atendente(self, cod_atendente):
        logging.info("Deletando atendente com código %s.", cod_atendente)
        try:
            resultado = self.atendente_model.deletar_atendente(cod_atendente)
            if not resultado:
                return {"message": f"Atendente com código {cod_atendente} não encontrado.", "status": "error"}
            return {"message": "Atendente deletado com sucesso.", "status": "success"}
        except Exception as e:
            logging.error("Erro ao deletar atendente: %s", e)
            raise
