from tkinter import Frame, Label, Entry, Button
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AtendimentoView:
    def __init__(self, master, controller):
        logging.info("Inicializando a visualização de atendimento.")
        self.controller = controller
        self.cod_atendimento = 1  # Exemplo de código; ajuste conforme necessário
        self.frame_atendimento = Frame(master)
        self.frame_atendimento.pack(expand=True, fill="both")

        # Inicializa os widgets de visualização de dados
        self.init_view_widgets()

        # Carregar dados iniciais
        self.carregar_dados()

    def init_view_widgets(self):
        # Exibir dados do atendimento
        Label(self.frame_atendimento, text="Código do Atendimento:", font="Inter 9 bold", fg="#0B033F").place(x=90, y=120)
        self.label_cod_atendimento = Label(self.frame_atendimento, font="Inter 9 bold", fg="black")
        self.label_cod_atendimento.place(x=210, y=120)

        Label(self.frame_atendimento, text="CPF do Paciente:", font="Inter 9 bold", fg="#0B033F").place(x=90, y=145)
        self.label_cpf_paciente = Label(self.frame_atendimento, font="Inter 9 bold", fg="black")
        self.label_cpf_paciente.place(x=210, y=145)

        Label(self.frame_atendimento, text="CRM do Médico:", font="Inter 9 bold", fg="#0B033F").place(x=90, y=170)
        self.label_crm_medico = Label(self.frame_atendimento, font="Inter 9 bold", fg="black")
        self.label_crm_medico.place(x=210, y=170)

        # Botões para cadastrar e alterar
        Button(self.frame_atendimento, text="Cadastrar", width=10, font="Inter 8 bold", fg="white", bg="#0B033F", command=self.cadastrar_atendimento).place(x=90, y=225)
        Button(self.frame_atendimento, text="Alterar", width=10, font="Inter 8 bold", fg="white", bg="#0B033F", command=self.alterar_atendimento).place(x=200, y=225)

    def carregar_dados(self):
        logging.info("Carregando dados do atendimento com código: %s", self.cod_atendimento)
        try:
            atendimento = self.controller.buscar_atendimento_por_codigo(self.cod_atendimento)
            if atendimento:
                atendimento_data = atendimento[0]
                self.label_cod_atendimento.config(text=atendimento_data['cod_atendimento'])
                self.label_cpf_paciente.config(text=atendimento_data['cpf_paciente'])
                self.label_crm_medico.config(text=atendimento_data['crm'])
            else:
                logging.info("Nenhum atendimento encontrado.")
                self.label_cod_atendimento.config(text="Não encontrado")
                self.label_cpf_paciente.config(text="Não encontrado")
                self.label_crm_medico.config(text="Não encontrado")
        except Exception as e:
            logging.error("Erro ao carregar dados do atendimento: %s", e)

    def cadastrar_atendimento(self):
        logging.info("Iniciando o cadastro de um novo atendimento.")
        # Código para abrir o formulário de cadastro de atendimento.
        # Exemplo:
        for widget in self.frame_atendimento.winfo_children():
            widget.destroy()

        Label(self.frame_atendimento, text="CPF do Paciente:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=30)
        entry_cpf_paciente = Entry(self.frame_atendimento, width=35)
        entry_cpf_paciente.place(x=15, y=60)

        Label(self.frame_atendimento, text="CRM do Médico:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=90)
        entry_crm_medico = Entry(self.frame_atendimento, width=35)
        entry_crm_medico.place(x=15, y=120)

        # Botão para salvar o novo atendimento
        Button(self.frame_atendimento, text="Salvar", width=10, font="Inter 8 bold", fg="white", bg="#0B033F",
               command=lambda: self.salvar_cadastro(entry_cpf_paciente.get(), entry_crm_medico.get())).place(x=85, y=180)

    def salvar_cadastro(self, cpf_paciente, crm_medico):
        try:
            # Assumindo que o método `inserir_atendimento` do controller faz o cadastro no banco de dados
            self.controller.inserir_atendimento(self.cod_atendimento, cpf_paciente, crm_medico)
            logging.info("Novo atendimento cadastrado com sucesso.")
            self.carregar_dados()  # Recarrega os dados após salvar
        except Exception as e:
            logging.error("Erro ao cadastrar atendimento: %s", e)

    def alterar_atendimento(self):
        logging.info("Usuário iniciou alteração de dados do atendimento.")
        # Implemente a lógica para o formulário de alteração de atendimento se necessário.
