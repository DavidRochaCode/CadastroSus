from models.atendimento_model import AtendimentoModel
import logging

class AtendimentoController:
    def __init__(self, atendimento_model: AtendimentoModel):
        self.atendimento_model = atendimento_model

    def inserir_atendimento(self, cod_atendimento, cpf_paciente, crm):
        logging.info("Inserindo atendimento com código %s, CPF do paciente: %s, CRM do médico: %s", cod_atendimento, cpf_paciente, crm)
        try:
            self.atendimento_model.inserir_atendimento(cod_atendimento, cpf_paciente, crm)
            logging.info("Atendimento inserido com sucesso.")
        except Exception as e:
            logging.error("Erro ao inserir atendimento: %s", e)
            raise

    def buscar_atendimento_por_codigo(self, cod_atendimento):
        logging.info("Buscando atendimento com código %s", cod_atendimento)
        try:
            atendimento = self.atendimento_model.buscar_atendimento_por_codigo(cod_atendimento)
            logging.info("Atendimento encontrado: %s", atendimento)
            return atendimento
        except Exception as e:
            logging.error("Erro ao buscar atendimento: %s", e)
            raise

    def deletar_atendimento(self, cod_atendimento):
        logging.info("Deletando atendimento com código %s", cod_atendimento)
        try:
            self.atendimento_model.deletar_atendimento(cod_atendimento)
            logging.info("Atendimento deletado com sucesso.")
        except Exception as e:
            logging.error("Erro ao deletar atendimento: %s", e)
            raise
