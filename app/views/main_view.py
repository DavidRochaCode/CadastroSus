from tkinter import ttk, Frame
from views.atendente_view import AtendenteView
from views.paciente_view import PacienteView
from views.medico_view import MedicoView
from views.atendimento_view import AtendimentoView
from views.admin_view import AdminView  # Importa a AdminView

class MainView:
    def __init__(self, master, atendente_controller, medico_controller, paciente_controller, atendimento_controller):
        self.master = master
        self.master.title("Sistema de Gestão UBS")

        # Criação do notebook para as abas
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill='both')

        # Frame para cada aba
        self.frame_atendente = Frame(self.notebook)
        self.frame_medico = Frame(self.notebook)
        self.frame_paciente = Frame(self.notebook)
        self.frame_atendimento = Frame(self.notebook)
        self.frame_admin = Frame(self.notebook)  # Adicionando a frame Admin

        # Adiciona cada aba ao notebook
        self.notebook.add(self.frame_atendente, text="Atendente")
        self.notebook.add(self.frame_medico, text="Médico")
        self.notebook.add(self.frame_paciente, text="Paciente")
        self.notebook.add(self.frame_atendimento, text="Atendimento")
        self.notebook.add(self.frame_admin, text="Administração")  # Aba para administração

        # Inicializa as views para cada aba
        self.atendente_view = AtendenteView(self.frame_atendente, atendente_controller)
        self.medico_view = MedicoView(self.frame_medico, medico_controller)
        self.paciente_view = PacienteView(self.frame_paciente, paciente_controller)
        self.atendimento_view = AtendimentoView(self.frame_atendimento, atendimento_controller)
        self.admin_view = AdminView(self.frame_admin, medico_controller, paciente_controller, atendente_controller, atendimento_controller)
