from tkinter import Frame, Label, Entry, Button
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MedicoView:
    def __init__(self, master, controller):
        logging.info("Inicializando a visualização de médico.")
        self.controller = controller
        self.crm_medico = 1234  # Exemplo de CRM; ajuste conforme necessário
        self.frame_medico = Frame(master)
        self.frame_medico.pack(expand=True, fill="both")

        # Inicializa os widgets de visualização de dados
        self.init_view_widgets()

        # Carregar dados iniciais
        self.carregar_dados()

    def init_view_widgets(self):
        # Exibir dados do médico
        Label(self.frame_medico, text="Nome:", font="Inter 9 bold", fg="#0B033F").place(x=90, y=120)
        self.label_nome = Label(self.frame_medico, font="Inter 9 bold", fg="black")
        self.label_nome.place(x=130, y=120)

        Label(self.frame_medico, text="CRM:", font="Inter 9 bold", fg="#0B033F").place(x=90, y=145)
        self.label_crm = Label(self.frame_medico, font="Inter 9 bold", fg="black")
        self.label_crm.place(x=130, y=145)

        Label(self.frame_medico, text="Atuação:", font="Inter 9 bold", fg="#0B033F").place(x=90, y=170)
        self.label_atuacao = Label(self.frame_medico, font="Inter 9 bold", fg="black")
        self.label_atuacao.place(x=160, y=170)

        Button(self.frame_medico, text="Alterar", width=10, font="Inter 8 bold", fg="white", bg="#0B033F", command=self.alterar_medico).place(x=175, y=225)

    def carregar_dados(self):
        logging.info("Carregando dados do médico com CRM: %s", self.crm_medico)
        try:
            medico = self.controller.buscar_medico_por_crm(self.crm_medico)
            if medico:
                self.label_nome.config(text=medico[0][1])  # nome
                self.label_crm.config(text=medico[0][0])   # crm
                self.label_atuacao.config(text=medico[0][3])  # atuacao
            else:
                logging.info("Nenhum médico encontrado.")
                self.label_nome.config(text="Não encontrado")
                self.label_crm.config(text="Não encontrado")
                self.label_atuacao.config(text="Não encontrado")
        except Exception as e:
            logging.error("Erro ao carregar dados do médico: %s", e)

    def alterar_medico(self):
        logging.info("Usuário iniciou alteração de dados do médico.")
        for widget in self.frame_medico.winfo_children():
            widget.destroy()

        Label(self.frame_medico, text="Nome:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=30)
        entry_nome = Entry(self.frame_medico, width=35)
        entry_nome.place(x=15, y=60)

        Label(self.frame_medico, text="CRM:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=90)
        entry_crm = Entry(self.frame_medico, width=35)
        entry_crm.place(x=15, y=120)

        Label(self.frame_medico, text="Atuação:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=150)
        entry_atuacao = Entry(self.frame_medico, width=35)
        entry_atuacao.place(x=15, y=180)

        Button(self.frame_medico, text="Salvar", width=10, font="Inter 8 bold", fg="white", bg="#0B033F", command=lambda: self.salvar_alteracoes(entry_nome.get(), entry_crm.get(), entry_atuacao.get())).place(x=85, y=220)

    def salvar_alteracoes(self, nome, crm, atuacao):
        logging.info("Salvando alterações do médico: Nome: %s, CRM: %s, Atuação: %s", nome, crm, atuacao)
        try:
            self.controller.atualizar_medico(crm, nome, atuacao)
            logging.info("Alterações salvas com sucesso.")
        except Exception as e:
            logging.error("Erro ao salvar alterações do médico: %s", e)

        for widget in self.frame_medico.winfo_children():
            widget.destroy()
        self.init_view_widgets()
        self.carregar_dados()
