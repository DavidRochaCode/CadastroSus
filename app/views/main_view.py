from tkinter import Frame, Label, ttk
from views.atendente_view import AtendenteView
from views.medico_view import MedicoView
from views.paciente_view import PacienteView
from views.atendimento_view import AtendimentoView

class MainView:
    def __init__(self, root, atendente_controller, medico_controller, paciente_controller, atendimento_controller):
        self.root = root
        self.root.title("UBS Garanhuns")
        self.root.geometry("542x460")
        self.root.resizable(False, False)

        # Cabeçalho
        self.setup_header()

        # Criação das abas
        self.tab_control = ttk.Notebook(self.root, width=430, height=315)
        self.tab_control.place(x=50, y=85)

        # Abas específicas para cada módulo
        self.tab_atendente = Frame(self.tab_control)
        self.tab_paciente = Frame(self.tab_control)
        self.tab_medico = Frame(self.tab_control)
        self.tab_atendimento = Frame(self.tab_control)

        # Adiciona as abas ao controle de abas
        self.tab_control.add(self.tab_atendente, text="Atendente")
        self.tab_control.add(self.tab_paciente, text="Paciente")
        self.tab_control.add(self.tab_medico, text="Médico")
        self.tab_control.add(self.tab_atendimento, text="Atendimento")

        # Inicializa cada visualização diretamente nas suas respectivas abas
        AtendenteView(self.tab_atendente, atendente_controller)
        PacienteView(self.tab_paciente, paciente_controller)
        MedicoView(self.tab_medico, medico_controller)
        AtendimentoView(self.tab_atendimento, atendimento_controller)

        # Rodapé
        self.setup_footer()

    def setup_header(self):
        header_frame = Frame(self.root, width=542, height=85, bg="#0B033F")
        header_frame.place(x=0, y=0)

        label_ubs = Label(header_frame, text="UBS", font="Inter 32 italic bold underline", fg="white", bg="#0B033F")
        label_ubs.place(x=150, y=18)

        label_garanhuns = Label(header_frame, text="Garanhuns", font="Inter 25", fg="white", bg="#0B033F")
        label_garanhuns.place(x=253, y=28)

    def setup_footer(self):
        footer_frame = Frame(self.root, width=542, height=35, bg="#0B033F")
        footer_frame.place(x=0, y=426)

        label_footer = Label(
            footer_frame,
            text="Endereço: R. Sebastião Paes de Melo, 581-601 - Heliópolis, Garanhuns - PE, 55298-520",
            font="Inter 6",
            fg="white",
            bg="#0B033F"
        )
        label_footer.place(x=10, y=9)
