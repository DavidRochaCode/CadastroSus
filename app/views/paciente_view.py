from tkinter import Frame, Label, Entry, Button, ttk, messagebox, Canvas, Scrollbar
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PacienteView:
    def __init__(self, master, controller):
        logging.info("Inicializando a visualização de paciente.")
        self.controller = controller
        self.frame_paciente = Frame(master)
        self.frame_paciente.pack(expand=True, fill="both")

        # Cria o notebook com abas
        self.notebook = ttk.Notebook(self.frame_paciente)
        self.notebook.pack(expand=True, fill="both")

        # Cria as abas
        self.frame_consultar = Frame(self.notebook)
        self.frame_cadastrar = Frame(self.notebook)
        
        self.notebook.add(self.frame_consultar, text="Consultar Paciente")
        self.notebook.add(self.frame_cadastrar, text="Cadastrar Paciente")

        # Inicializa widgets para cada aba
        self.init_consultar_widgets()
        self.init_cadastrar_widgets()

    def init_consultar_widgets(self):
        Label(self.frame_consultar, text="CPF:", font="Inter 9 bold", fg="#0B033F").place(x=10, y=10)
        self.entry_cpf_consulta = Entry(self.frame_consultar, width=20)
        self.entry_cpf_consulta.place(x=50, y=10)
        
        Button(self.frame_consultar, text="Buscar", command=self.consultar_paciente).place(x=200, y=7)
        
        self.label_nome = Label(self.frame_consultar, text="Nome: ", font="Inter 9 bold", fg="black")
        self.label_nome.place(x=10, y=50)
        self.label_cpf = Label(self.frame_consultar, text="CPF: ", font="Inter 9 bold", fg="black")
        self.label_cpf.place(x=10, y=80)
        self.label_endereco = Label(self.frame_consultar, text="Endereço: ", font="Inter 9 bold", fg="black")
        self.label_endereco.place(x=10, y=110)

    def init_cadastrar_widgets(self):
        # Configuração de canvas e scrollbar para rolagem
        canvas = Canvas(self.frame_cadastrar)
        scrollbar = Scrollbar(self.frame_cadastrar, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Widgets de cadastro no frame rolável
        Label(scrollable_frame, text="Nome:", font="Inter 10 bold", fg="#0B033F").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_nome = Entry(scrollable_frame, width=35)
        self.entry_nome.pack(anchor="w", padx=10)

        Label(scrollable_frame, text="Sobrenome:", font="Inter 10 bold", fg="#0B033F").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_sobrenome = Entry(scrollable_frame, width=35)
        self.entry_sobrenome.pack(anchor="w", padx=10)

        Label(scrollable_frame, text="CPF:", font="Inter 10 bold", fg="#0B033F").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_cpf = Entry(scrollable_frame, width=35)
        self.entry_cpf.pack(anchor="w", padx=10)

        Label(scrollable_frame, text="Endereço:", font="Inter 10 bold", fg="#0B033F").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_endereco = Entry(scrollable_frame, width=35)
        self.entry_endereco.pack(anchor="w", padx=10)

        Label(scrollable_frame, text="Celular:", font="Inter 10 bold", fg="#0B033F").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_celular = Entry(scrollable_frame, width=35)
        self.entry_celular.pack(anchor="w", padx=10)

        Label(scrollable_frame, text="Cartão SUS:", font="Inter 10 bold", fg="#0B033F").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_cartao_sus = Entry(scrollable_frame, width=35)
        self.entry_cartao_sus.pack(anchor="w", padx=10)

        Label(scrollable_frame, text="Prontuário:", font="Inter 10 bold", fg="#0B033F").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_prontuario = Entry(scrollable_frame, width=35)
        self.entry_prontuario.pack(anchor="w", padx=10)

        Button(scrollable_frame, text="Salvar", width=10, font="Inter 8 bold", fg="white", bg="#0B033F", command=self.cadastrar_paciente).pack(pady=20)

    def consultar_paciente(self):
        cpf = self.entry_cpf_consulta.get()
        if cpf:
            logging.info("Buscando paciente com CPF: %s", cpf)
            paciente = self.controller.buscar_paciente(cpf)
            if paciente:
                self.label_nome.config(text=f"Nome: {paciente[0][0]} {paciente[0][1]}")  # nome e sobrenome
                self.label_cpf.config(text=f"CPF: {paciente[0][4]}")  # cpf_paciente
                self.label_endereco.config(text=f"Endereço: {paciente[0][3]}")  # endereco
            else:
                messagebox.showinfo("Paciente não encontrado", "Nenhum paciente encontrado com o CPF fornecido.")
        else:
            messagebox.showwarning("CPF Vazio", "Por favor, insira o CPF do paciente.")

    def cadastrar_paciente(self):
        nome = self.entry_nome.get()
        sobrenome = self.entry_sobrenome.get()
        cpf = self.entry_cpf.get()
        endereco = self.entry_endereco.get()
        celular = self.entry_celular.get()
        cartao_sus = self.entry_cartao_sus.get()
        prontuario = self.entry_prontuario.get()

        if nome and sobrenome and cpf and endereco and celular and cartao_sus and prontuario:
            try:
                self.controller.inserir_paciente(nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario)
                messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
            except Exception as e:
                logging.error("Erro ao cadastrar paciente: %s", e)
                messagebox.showerror("Erro", "Erro ao cadastrar paciente.")
        else:
            messagebox.showwarning("Campos vazios", "Por favor, preencha todos os campos para cadastrar o paciente.")
