from tkinter import Frame, Label, Entry, Button
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PacienteView:
    def __init__(self, master, controller):
        logging.info("Inicializando a visualização de paciente.")
        self.controller = controller
        self.cpf_paciente = "12345678901"  # Exemplo de CPF; ajuste conforme necessário
        self.frame_paciente = Frame(master)
        self.frame_paciente.pack(expand=True, fill="both")

        # Inicializa os widgets de visualização de dados
        self.init_view_widgets()

        # Carregar dados iniciais
        self.carregar_dados()

    def init_view_widgets(self):
        # Exibir dados do paciente
        Label(self.frame_paciente, text="Nome:", font="Inter 9 bold", fg="#0B033F").place(x=90, y=120)
        self.label_nome = Label(self.frame_paciente, font="Inter 9 bold", fg="black")
        self.label_nome.place(x=130, y=120)

        Label(self.frame_paciente, text="CPF:", font="Inter 9 bold", fg="#0B033F").place(x=90, y=145)
        self.label_cpf = Label(self.frame_paciente, font="Inter 9 bold", fg="black")
        self.label_cpf.place(x=130, y=145)

        Label(self.frame_paciente, text="Endereço:", font="Inter 9 bold", fg="#0B033F").place(x=90, y=170)
        self.label_endereco = Label(self.frame_paciente, font="Inter 9 bold", fg="black")
        self.label_endereco.place(x=160, y=170)

        Button(self.frame_paciente, text="Alterar", width=10, font="Inter 8 bold", fg="white", bg="#0B033F", command=self.alterar_paciente).place(x=175, y=225)

    def carregar_dados(self):
        logging.info("Carregando dados do paciente com CPF: %s", self.cpf_paciente)
        try:
            paciente = self.controller.buscar_paciente(self.cpf_paciente)
            if paciente:
                self.label_nome.config(text=f"{paciente[0]['nome']} {paciente[0]['sobrenome']}")
                self.label_cpf.config(text=paciente[0]['cpf_paciente'])
                self.label_endereco.config(text=paciente[0]['endereco'])
            else:
                logging.info("Nenhum paciente encontrado.")
                self.label_nome.config(text="Não encontrado")
                self.label_cpf.config(text="Não encontrado")
                self.label_endereco.config(text="Não encontrado")
        except Exception as e:
            logging.error("Erro ao carregar dados do paciente: %s", e)

    def alterar_paciente(self):
        logging.info("Usuário iniciou alteração de dados do paciente.")
        for widget in self.frame_paciente.winfo_children():
            widget.destroy()

        Label(self.frame_paciente, text="Nome:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=30)
        entry_nome = Entry(self.frame_paciente, width=35)
        entry_nome.place(x=15, y=60)

        Label(self.frame_paciente, text="Sobrenome:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=90)
        entry_sobrenome = Entry(self.frame_paciente, width=35)
        entry_sobrenome.place(x=15, y=120)

        Label(self.frame_paciente, text="CPF:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=150)
        entry_cpf = Entry(self.frame_paciente, width=35)
        entry_cpf.place(x=15, y=180)

        Label(self.frame_paciente, text="Endereço:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=210)
        entry_endereco = Entry(self.frame_paciente, width=35)
        entry_endereco.place(x=15, y=240)

        Button(self.frame_paciente, text="Salvar", width=10, font="Inter 8 bold", fg="white", bg="#0B033F", command=lambda: self.salvar_alteracoes(entry_nome.get(), entry_sobrenome.get(), entry_cpf.get(), entry_endereco.get())).place(x=85, y=280)

    def salvar_alteracoes(self, nome, sobrenome, cpf, endereco):
        logging.info("Salvando alterações do paciente: %s %s, CPF: %s", nome, sobrenome, cpf)
        try:
            self.controller.alterar_paciente(nome, sobrenome, cpf, endereco)
            logging.info("Alterações salvas com sucesso.")
        except Exception as e:
            logging.error("Erro ao salvar alterações do paciente: %s", e)

        for widget in self.frame_paciente.winfo_children():
            widget.destroy()
        self.init_view_widgets()
        self.carregar_dados()
