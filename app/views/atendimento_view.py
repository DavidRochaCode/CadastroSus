from tkinter import Canvas, Frame, Label, Entry, Button, ttk, messagebox
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AtendimentoView:
    def __init__(self, master, controller):
        logging.info("Inicializando a visualização de atendimento.")
        self.controller = controller
        self.frame_atendimento = Frame(master)
        self.frame_atendimento.pack(expand=True, fill="both")

        # Cria o notebook com abas
        self.notebook = ttk.Notebook(self.frame_atendimento)
        self.notebook.pack(expand=True, fill="both")

        # Cria as abas
        self.frame_cadastrar = Frame(self.notebook)
        self.frame_consultar = Frame(self.notebook)
        
        self.notebook.add(self.frame_cadastrar, text="Cadastrar Atendimento")
        self.notebook.add(self.frame_consultar, text="Consultar Atendimento")

        # Inicializa widgets para cada aba
        self.init_cadastrar_widgets()
        self.init_consultar_widgets()

    def init_cadastrar_widgets(self):
        Label(self.frame_cadastrar, text="CPF do Paciente:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=10)
        self.entry_cpf_paciente = Entry(self.frame_cadastrar, width=35)
        self.entry_cpf_paciente.place(x=10, y=30)

        Label(self.frame_cadastrar, text="Código do Atendimento:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=60)
        self.entry_cod_atendimento = Entry(self.frame_cadastrar, width=35)
        self.entry_cod_atendimento.place(x=10, y=80)

        Label(self.frame_cadastrar, text="CRM do Médico:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=110)
        self.entry_crm_medico = Entry(self.frame_cadastrar, width=35)
        self.entry_crm_medico.place(x=10, y=130)

        Button(self.frame_cadastrar, text="Salvar", width=10, font="Inter 8 bold", fg="white", bg="#0B033F",
               command=self.cadastrar_atendimento).place(x=100, y=170)

    def init_consultar_widgets(self):
        # Configuração do Canvas com Scrollbar
        canvas = Canvas(self.frame_consultar)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(self.frame_consultar, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Frame interno dentro do Canvas
        self.scrollable_frame = Frame(canvas)
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Widgets no Frame rolável
        Label(self.scrollable_frame, text="Código do Atendimento:", font="Inter 10 bold", fg="#0B033F").grid(row=0, column=0, pady=5, sticky="w")
        self.entry_cod_consulta = Entry(self.scrollable_frame, width=35)
        self.entry_cod_consulta.grid(row=0, column=1, pady=5)

        Button(self.scrollable_frame, text="Consultar", width=10, font="Inter 8 bold", fg="white", bg="#0B033F",
            command=self.consultar_atendimento).grid(row=1, column=0, columnspan=2, pady=5)

        # Campos para exibir informações do atendimento
        self.label_cod_atendimento = Label(self.scrollable_frame, text="Código: ", font="Inter 9 bold", fg="black")
        self.label_cod_atendimento.grid(row=2, column=0, pady=5, sticky="w")
        self.label_data_atendimento = Label(self.scrollable_frame, text="Data: ", font="Inter 9 bold", fg="black")
        self.label_data_atendimento.grid(row=3, column=0, pady=5, sticky="w")
        self.label_cpf_paciente = Label(self.scrollable_frame, text="CPF do Paciente: ", font="Inter 9 bold", fg="black")
        self.label_cpf_paciente.grid(row=4, column=0, pady=5, sticky="w")
        self.label_nome_paciente = Label(self.scrollable_frame, text="Nome do Paciente: ", font="Inter 9 bold", fg="black")
        self.label_nome_paciente.grid(row=5, column=0, pady=5, sticky="w")
        self.label_sobrenome_paciente = Label(self.scrollable_frame, text="Sobrenome do Paciente: ", font="Inter 9 bold", fg="black")
        self.label_sobrenome_paciente.grid(row=6, column=0, pady=5, sticky="w")
        self.label_celular_paciente = Label(self.scrollable_frame, text="Celular do Paciente: ", font="Inter 9 bold", fg="black")
        self.label_celular_paciente.grid(row=7, column=0, pady=5, sticky="w")
        self.label_nome_medico = Label(self.scrollable_frame, text="Nome do Médico: ", font="Inter 9 bold", fg="black")
        self.label_nome_medico.grid(row=8, column=0, pady=5, sticky="w")
        self.label_atuacao_medico = Label(self.scrollable_frame, text="Atuação do Médico: ", font="Inter 9 bold", fg="black")
        self.label_atuacao_medico.grid(row=9, column=0, pady=5, sticky="w")
        self.label_crm_medico = Label(self.scrollable_frame, text="CRM do Médico: ", font="Inter 9 bold", fg="black")
        self.label_crm_medico.grid(row=10, column=0, pady=5, sticky="w")


    def cadastrar_atendimento(self):
        cod_atendimento = self.entry_cod_atendimento.get()
        cpf_paciente = self.entry_cpf_paciente.get()
        crm_medico = self.entry_crm_medico.get()

        if cod_atendimento and cpf_paciente and crm_medico:
            try:
                self.controller.inserir_atendimento(cod_atendimento, cpf_paciente, crm_medico)
                messagebox.showinfo("Sucesso", "Atendimento cadastrado com sucesso!")
            except Exception as e:
                logging.error("Erro ao cadastrar atendimento: %s", e)
                messagebox.showerror("Erro", "Erro ao cadastrar atendimento.")
        else:
            messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos para cadastrar o atendimento.")

    def consultar_atendimento(self):
        cod_atendimento = self.entry_cod_consulta.get()
        if cod_atendimento:
            logging.info("Buscando atendimento com código: %s", cod_atendimento)
            try:
                atendimento = self.controller.buscar_atendimento_por_codigo(cod_atendimento)
                if atendimento:
                    atendimento_data = atendimento[0]
                    self.label_cod_atendimento.config(text=f"Código: {atendimento_data[0]}")
                    self.label_data_atendimento.config(text=f"Data: {atendimento_data[1]}")
                    self.label_cpf_paciente.config(text=f"CPF do Paciente: {atendimento_data[7]}")
                    self.label_crm_medico.config(text=f"CRM do Médico: {atendimento_data[10]}")
                    
                    # Novos campos
                    self.label_nome_paciente.config(text=f"Nome do Paciente: {atendimento_data[2]}")
                    self.label_sobrenome_paciente.config(text=f"Sobrenome do Paciente: {atendimento_data[3]}")
                    self.label_celular_paciente.config(text=f"Celular do Paciente: {atendimento_data[4]}")
                    self.label_nome_medico.config(text=f"Nome do Médico: {atendimento_data[8]}")
                    self.label_atuacao_medico.config(text=f"Atuação do Médico: {atendimento_data[9]}")
                else:
                    messagebox.showinfo("Atendimento não encontrado", "Nenhum atendimento encontrado com o código fornecido.")
            except Exception as e:
                logging.error("Erro ao buscar atendimento: %s", e)
                messagebox.showerror("Erro", "Erro ao consultar atendimento.")
        else:
            messagebox.showwarning("Código Vazio", "Por favor, insira o código do atendimento.")
