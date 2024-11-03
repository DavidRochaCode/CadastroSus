from models.atendente_model import AtendenteModel
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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

    def inserir_atendente(self, nome, sobrenome, codigo):
        logging.info("Inserindo atendente: %s %s, Código: %s", nome, sobrenome, codigo)
        try:
            self.atendente_model.inserir_atendente(nome, sobrenome, codigo)
            logging.info("Atendente inserido com sucesso.")
        except Exception as e:
            logging.error("Erro ao inserir atendente: %s", e)
            raise

    def alterar_atendente(self, nome, sobrenome, codigo, cod_controle):
        logging.info("Alterando atendente: %s %s, Código: %s, Controle: %s", nome, sobrenome, codigo, cod_controle)
        try:
            self.atendente_model.atualizar_atendente(nome, sobrenome, codigo, cod_controle)
            logging.info("Atendente atualizado com sucesso.")
        except Exception as e:
            logging.error("Erro ao atualizar atendente: %s", e)
            raise
