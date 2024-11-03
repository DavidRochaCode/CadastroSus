from models.medico_model import MedicoModel
import logging

class MedicoController:
    def __init__(self, medico_model: MedicoModel):
        self.medico_model = medico_model

    def atualizar_medico(self, crm, nome, atuacao):
        logging.info("Atualizando médico com CRM %s: Nome = %s, Atuação = %s", crm, nome, atuacao)
        try:
            self.medico_model.atualizar_medico(crm, nome, atuacao)
            logging.info("Médico atualizado com sucesso.")
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

    def inserir_medico(self, crm, nome, atuacao):
        logging.info("Inserindo médico com CRM %s: Nome = %s, Atuação = %s", crm, nome, atuacao)
        try:
            self.medico_model.inserir_medico(crm, nome, atuacao)
            logging.info("Médico inserido com sucesso.")
        except Exception as e:
            logging.error("Erro ao inserir médico: %s", e)
            raise
