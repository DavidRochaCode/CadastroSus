from models.paciente_model import PacienteModel
import logging

class PacienteController:
    def __init__(self, model: PacienteModel):
        self.model = model

    def buscar_paciente(self, cpf):
        logging.info("Buscando paciente com CPF: %s", cpf)
        try:
            paciente = self.model.buscar_paciente_por_cpf(cpf)
            logging.info("Paciente encontrado: %s", paciente)
            return paciente
        except Exception as e:
            logging.error("Erro ao buscar paciente: %s", e)
            raise

    def inserir_paciente(self, nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario):
        logging.info("Inserindo paciente: Nome = %s %s, CPF = %s", nome, sobrenome, cpf)
        try:
            self.model.inserir_paciente(nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario)
            logging.info("Paciente inserido com sucesso.")
        except Exception as e:
            logging.error("Erro ao inserir paciente: %s", e)
            raise

    def alterar_paciente(self, nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario):
        logging.info("Atualizando paciente com CPF: %s", cpf)
        try:
            self.model.atualizar_paciente(nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario)
            logging.info("Paciente atualizado com sucesso.")
        except Exception as e:
            logging.error("Erro ao atualizar paciente: %s", e)
            raise
