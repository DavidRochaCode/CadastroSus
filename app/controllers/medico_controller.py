from app.models.medico_model import MedicoModel
import logging

class MedicoController:
    def __init__(self, medico_model: MedicoModel):
        self.medico_model = medico_model

    def atualizar_medico(self, crm, nome, atuacao):
        logging.info("Atualizando médico com CRM %s: Nome = %s, Atuação = %s", crm, nome, atuacao)
        try:
            resultado = self.medico_model.atualizar_medico(crm, nome, atuacao)
            if not resultado:
                return {"message": f"Médico com CRM {crm} não encontrado.", "status": "error"}
            return {"message": f"Médico atualizado com sucesso.", "status": "success"}
        except Exception as e:
            logging.error("Erro ao atualizar médico: %s", e)
            raise

    def buscar_medico_por_crm(self, crm):
        logging.info("Buscando médico com CRM %s", crm)
        try:
            medico = self.medico_model.buscar_medico_por_crm(crm)
            logging.info("Médico encontrado: %s", medico)
            return medico
        except Exception as e:
            logging.error("Erro ao buscar médico: %s", e)
            raise
    def buscar_todos_medicos(self):
        logging.info("Buscando todos os médicos.")
        try:
            medicos = self.medico_model.buscar_todos_medicos()
            logging.info("Médicos encontrados: %s", medicos)
            return medicos
        except Exception as e:
            logging.error("Erro ao buscar médicos: %s", e)
            raise

    def inserir_medico(self, crm, nome, atuacao):
        logging.info("Inserindo médico com CRM %s: Nome = %s, Atuação = %s", crm, nome, atuacao)
        try:
            resultado = self.medico_model.inserir_medico(crm, nome, atuacao)
            if resultado:
                return {"message": f"Médico com CRM {crm} já existe.", "status": "error"}
            return {"message": "Médico cadastrado com sucesso.", "status": "success"}
        except Exception as e:
            logging.error("Erro ao inserir médico: %s", e)
            raise

    def deletar_medico(self, crm):
        logging.info("Deletando médico com CRM %s", crm)
        try:
            resultado = self.medico_model.deletar_medico(crm)
            if not resultado:
                return {"message": f"Médico com CRM {crm} não encontrado.", "status": "error"}
            return {"message": f"Médico deletado.", "status": "success"}
        except Exception as e:
            logging.error("Erro ao deletar médico: %s", e)
            raise
