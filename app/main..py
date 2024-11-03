import logging
from tkinter import Tk
from models.database import Database

# Configura o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Importa modelos e controladores
from models.atendente_model import AtendenteModel
from controllers.atendente_controller import AtendenteController

from models.medico_model import MedicoModel
from controllers.medico_controller import MedicoController

from models.paciente_model import PacienteModel
from controllers.paciente_controller import PacienteController

from models.atendimento_model import AtendimentoModel
from controllers.atendimento_controller import AtendimentoController

# Importa a MainView para exibir as abas
from views.main_view import MainView

def main():
    logging.info("Inicializando o banco de dados.")
    db = Database()

    # Configuração para Atendente
    logging.info("Configurando o modelo e controlador para Atendente.")
    atendente_model = AtendenteModel(db)
    atendente_model.criar_tabela()
    atendente_controller = AtendenteController(atendente_model)

    # Configuração para Médico
    logging.info("Configurando o modelo e controlador para Médico.")
    medico_model = MedicoModel(db)
    medico_model.criar_tabela()
    medico_controller = MedicoController(medico_model)

    # Configuração para Paciente
    logging.info("Configurando o modelo e controlador para Paciente.")
    paciente_model = PacienteModel(db)
    paciente_model.criar_tabela()
    paciente_controller = PacienteController(paciente_model)

    # Configuração para Atendimento
    logging.info("Configurando o modelo e controlador para Atendimento.")
    atendimento_model = AtendimentoModel(db)
    atendimento_model.criar_tabela()
    atendimento_controller = AtendimentoController(atendimento_model)

    # Interface principal com abas
    logging.info("Inicializando a interface principal com as abas.")
    root = Tk()
    MainView(root, atendente_controller, medico_controller, paciente_controller, atendimento_controller)

    # Inicia o loop principal da interface
    logging.info("Iniciando o loop principal da interface.")
    root.mainloop()

    # Fecha a conexão com o banco de dados
    logging.info("Fechando a conexão com o banco de dados.")
    db.close()

if __name__ == '__main__':
    logging.info("Iniciando a aplicação.")
    main()
    logging.info("Aplicação encerrada.")
