from app.models.atendimento_model import AtendimentoModel
import logging

class AtendimentoController:
    def __init__(self, atendimento_model: AtendimentoModel):
        self.atendimento_model = atendimento_model

    def inserir_atendimento(self, cod_atendimento, cpf_paciente, crm):
        logging.info("Inserindo atendimento com código %s, CPF do paciente: %s, CRM do médico: %s", cod_atendimento, cpf_paciente, crm)
        try:
            resultado = self.atendimento_model.inserir_atendimento(cod_atendimento, cpf_paciente, crm)
            if resultado == -1:  # CRM não encontrado
                logging.warning("CRM %s não encontrado. Operação abortada.", crm)
                return {"message": f"Atendimento não inserido. CRM {crm} não encontrado.", "status": "error"}
            if resultado == -2:  # CPF do paciente não encontrado
                logging.warning("CPF do paciente %s não encontrado. Operação abortada.", cpf_paciente)
                return {"message": f"Atendimento não inserido. CPF {cpf_paciente} não encontrado.", "status": "error"}
            logging.info("Atendimento inserido com sucesso.")
            return {"message": "Atendimento inserido com sucesso", "status": "success"}
        except Exception as e:
            logging.error("Erro ao inserir atendimento: %s", e)
            raise


    def buscar_atendimento_por_codigo(self, cod_atendimento: int):
        logging.info("Buscando atendimento com código %s", cod_atendimento)
        try:
            resultado = self.atendimento_model.buscar_atendimento_por_codigo(cod_atendimento)
            if resultado == -1:  # Atendimento não encontrado
                return {"message": f"Atendimento com código {cod_atendimento} não encontrado.", "status": "error"}
            logging.info("Atendimento encontrado: %s", resultado)
            return resultado
        except Exception as e:
            logging.error("Erro ao buscar atendimento: %s", e)
            raise


    def deletar_atendimento(self, cod_atendimento):
        logging.info("Deletando atendimento com código %s", cod_atendimento)
        try:
            resultado = self.atendimento_model.deletar_atendimento(cod_atendimento)
            if resultado == -1:  # CRM não encontrado
                return {"message": f"Atendimento não deletado. Cod {cod_atendimento} não encontrado.", "status": "error"}
            return {"message": "Atendimento deletado com sucesso", "status": "success"}
        except Exception as e:
            logging.error("Erro ao deletar atendimento: %s", e)
            raise
