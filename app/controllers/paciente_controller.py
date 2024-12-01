from app.models.paciente_model import PacienteModel
import logging

class PacienteController:
    def __init__(self, model: PacienteModel):
        self.model = model

    def buscar_paciente(self, cpf):
        logging.info("Buscando paciente com CPF: %s", cpf)
        try:
            paciente = self.model.buscar_paciente_por_cpf(cpf)
            if paciente is False:
                return {"message": f"Paciente com CPF {cpf} não existe", "status": "error"}
            logging.info("Paciente encontrado: %s", paciente)
            return {"data": paciente, "status": "success"}
        except Exception as e:
            logging.error("Erro ao buscar paciente: %s", e)
            raise


    def inserir_paciente(self, nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario):
        logging.info("Inserindo paciente: Nome = %s %s, CPF = %s", nome, sobrenome, cpf)
        try:
            resultado= self.model.inserir_paciente(nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario)
            if resultado:
                return {"message": f"Paciente com CPF {cpf} já existe", "status": "error"}
            return {"message": f"Paciente cadastrado com sucesso", "status": "success"}
        except Exception as e:
            logging.error("Erro ao inserir paciente: %s", e)
            raise

    def alterar_paciente(self, nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario, status):
        logging.info("Atualizando paciente com CPF: %s", cpf)
        try:
            resultado = self.model.atualizar_paciente(nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario, status)
            if not resultado:
                return {"message": f"Paciente com CPF {cpf} não encontrado.", "status": "error"}
            return {"message": f"Paciente atualizado com sucesso", "status": "success"}
        except Exception as e:
            logging.error("Erro ao atualizar paciente: %s", e)
            raise

    def deletar_paciente(self, cpf):
        logging.info("Deletando paciente com CPF %s", cpf)
        try:
            resultado = self.model.deletar_paciente(cpf)
            if not resultado:
                return {"message": f"Paciente com CPF {cpf} não encontrado.", "status": "error"}
            return {"message": f"Paciente deletado com sucesso", "status": "success"}
        except Exception as e:
            logging.error("Erro ao deletar paciente: %s", e)
            raise
