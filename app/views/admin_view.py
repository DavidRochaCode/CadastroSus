from tkinter import Frame, Label, Entry, Button, ttk, messagebox

class AdminView:
    def __init__(self, master, medico_controller, paciente_controller, atendente_controller, atendimento_controller):
        # Inicializando os controladores necessários
        self.medico_controller = medico_controller
        self.paciente_controller = paciente_controller
        self.atendente_controller = atendente_controller
        self.atendimento_controller = atendimento_controller

        # Frame principal
        self.frame_admin = Frame(master)
        self.frame_admin.pack(expand=True, fill="both")

        # Criação do notebook para gerenciar entidades
        self.notebook = ttk.Notebook(self.frame_admin)
        self.notebook.pack(expand=True, fill="both")

        # Criação das abas para Médico, Paciente, Atendente, Atendimento
        self.frame_medico = Frame(self.notebook)
        self.frame_paciente = Frame(self.notebook)
        self.frame_atendente = Frame(self.notebook)
        self.frame_atendimento = Frame(self.notebook)

        # Adicionando cada frame ao notebook
        self.notebook.add(self.frame_medico, text="Gerenciar Médicos")
        self.notebook.add(self.frame_paciente, text="Gerenciar Pacientes")
        self.notebook.add(self.frame_atendente, text="Gerenciar Atendentes")
        self.notebook.add(self.frame_atendimento, text="Gerenciar Atendimentos")

        # Inicializa widgets para cada aba
        self.init_medico_widgets()
        self.init_paciente_widgets()
        self.init_atendente_widgets()
        self.init_atendimento_widgets()

    ## MÉTODOS PARA MÉDICO ##
    def init_medico_widgets(self):
        # Widgets para o gerenciamento de médicos
        Label(self.frame_medico, text="CRM do Médico:", font="Inter 10 bold").grid(row=0, column=0, padx=10, pady=5)
        self.entry_crm_medico = Entry(self.frame_medico)
        self.entry_crm_medico.grid(row=0, column=1, padx=10, pady=5)

        Button(self.frame_medico, text="Buscar", command=self.buscar_medico).grid(row=0, column=2, padx=10, pady=5)
        Button(self.frame_medico, text="Deletar", command=self.deletar_medico).grid(row=0, column=3, padx=10, pady=5)

        Label(self.frame_medico, text="Nome:", font="Inter 10 bold").grid(row=1, column=0, padx=10, pady=5)
        self.entry_nome_medico = Entry(self.frame_medico)
        self.entry_nome_medico.grid(row=1, column=1, padx=10, pady=5)

        Label(self.frame_medico, text="Atuação:", font="Inter 10 bold").grid(row=2, column=0, padx=10, pady=5)
        self.entry_atuacao_medico = Entry(self.frame_medico)
        self.entry_atuacao_medico.grid(row=2, column=1, padx=10, pady=5)

        Button(self.frame_medico, text="Atualizar", command=self.atualizar_medico).grid(row=3, column=1, padx=10, pady=10)

    def buscar_medico(self):
        crm = self.entry_crm_medico.get()
        try:
            medico = self.medico_controller.buscar_medico_por_crm(crm)
            if medico:
                self.entry_nome_medico.delete(0, 'end')
                self.entry_nome_medico.insert(0, medico[0][1])
                self.entry_atuacao_medico.delete(0, 'end')
                self.entry_atuacao_medico.insert(0, medico[0][2])
            else:
                messagebox.showinfo("Médico não encontrado", "Nenhum médico encontrado com o CRM fornecido.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar médico: {e}")

    def atualizar_medico(self):
        crm = self.entry_crm_medico.get()
        nome = self.entry_nome_medico.get()
        atuacao = self.entry_atuacao_medico.get()
        try:
            self.medico_controller.atualizar_medico(crm, nome, atuacao)
            messagebox.showinfo("Sucesso", "Médico atualizado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar médico: {e}")

    def deletar_medico(self):
        crm = self.entry_crm_medico.get()
        try:
            self.medico_controller.deletar_medico(crm)
            messagebox.showinfo("Sucesso", "Médico deletado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar médico: {e}")

    ## MÉTODOS PARA PACIENTE ##
    def init_paciente_widgets(self):
        # Widgets para o gerenciamento de pacientes
        Label(self.frame_paciente, text="CPF do Paciente:", font="Inter 10 bold").grid(row=0, column=0, padx=10, pady=5)
        self.entry_cpf_paciente = Entry(self.frame_paciente)
        self.entry_cpf_paciente.grid(row=0, column=1, padx=10, pady=5)

        Button(self.frame_paciente, text="Buscar", command=self.buscar_paciente).grid(row=0, column=2, padx=10, pady=5)
        Button(self.frame_paciente, text="Deletar", command=self.deletar_paciente).grid(row=0, column=3, padx=10, pady=5)

        Label(self.frame_paciente, text="Nome:", font="Inter 10 bold").grid(row=1, column=0, padx=10, pady=5)
        self.entry_nome_paciente = Entry(self.frame_paciente)
        self.entry_nome_paciente.grid(row=1, column=1, padx=10, pady=5)

        Label(self.frame_paciente, text="Sobrenome:", font="Inter 10 bold").grid(row=2, column=0, padx=10, pady=5)
        self.entry_sobrenome_paciente = Entry(self.frame_paciente)
        self.entry_sobrenome_paciente.grid(row=2, column=1, padx=10, pady=5)

        Button(self.frame_paciente, text="Atualizar", command=self.atualizar_paciente).grid(row=3, column=1, padx=10, pady=10)

    def buscar_paciente(self):
        cpf = self.entry_cpf_paciente.get()
        try:
            paciente = self.paciente_controller.buscar_paciente(cpf)
            if paciente:
                self.entry_nome_paciente.delete(0, 'end')
                self.entry_nome_paciente.insert(0, paciente[0][0])
                self.entry_sobrenome_paciente.delete(0, 'end')
                self.entry_sobrenome_paciente.insert(0, paciente[0][1])
            else:
                messagebox.showinfo("Paciente não encontrado", "Nenhum paciente encontrado com o CPF fornecido.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar paciente: {e}")

    def atualizar_paciente(self):
        cpf = self.entry_cpf_paciente.get()
        nome = self.entry_nome_paciente.get()
        sobrenome = self.entry_sobrenome_paciente.get()
        try:
            self.paciente_controller.alterar_paciente(nome, sobrenome, cpf, "cartao_sus", "endereco", "celular", "prontuario")
            messagebox.showinfo("Sucesso", "Paciente atualizado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar paciente: {e}")

    def deletar_paciente(self):
        cpf = self.entry_cpf_paciente.get()
        try:
            self.paciente_controller.deletar_paciente(cpf)
            messagebox.showinfo("Sucesso", "Paciente deletado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar paciente: {e}")

    ## MÉTODOS PARA ATENDENTE ##
    def init_atendente_widgets(self):
        # Widgets para o gerenciamento de atendentes
        Label(self.frame_atendente, text="Código do Atendente:", font="Inter 10 bold").grid(row=0, column=0, padx=10, pady=5)
        self.entry_cod_atendente = Entry(self.frame_atendente)
        self.entry_cod_atendente.grid(row=0, column=1, padx=10, pady=5)

        Button(self.frame_atendente, text="Buscar", command=self.buscar_atendente).grid(row=0, column=2, padx=10, pady=5)
        Button(self.frame_atendente, text="Deletar", command=self.deletar_atendente).grid(row=0, column=3, padx=10, pady=5)

        Label(self.frame_atendente, text="Nome:", font="Inter 10 bold").grid(row=1, column=0, padx=10, pady=5)
        self.entry_nome_atendente = Entry(self.frame_atendente)
        self.entry_nome_atendente.grid(row=1, column=1, padx=10, pady=5)

        Label(self.frame_atendente, text="Sobrenome:", font="Inter 10 bold").grid(row=2, column=0, padx=10, pady=5)
        self.entry_sobrenome_atendente = Entry(self.frame_atendente)
        self.entry_sobrenome_atendente.grid(row=2, column=1, padx=10, pady=5)

        Button(self.frame_atendente, text="Atualizar", command=self.atualizar_atendente).grid(row=3, column=1, padx=10, pady=10)

    def buscar_atendente(self):
        cod_controle = self.entry_cod_atendente.get()
        try:
            atendentes = self.atendente_controller.buscar_atendentes()
            atendente = next((a for a in atendentes if a['cod_controle'] == int(cod_controle)), None)
            if atendente:
                self.entry_nome_atendente.delete(0, 'end')
                self.entry_nome_atendente.insert(0, atendente['nome'])
                self.entry_sobrenome_atendente.delete(0, 'end')
                self.entry_sobrenome_atendente.insert(0, atendente['sobrenome'])
            else:
                messagebox.showinfo("Atendente não encontrado", "Nenhum atendente encontrado com o código fornecido.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar atendente: {e}")

    def atualizar_atendente(self):
        cod_controle = self.entry_cod_atendente.get()
        nome = self.entry_nome_atendente.get()
        sobrenome = self.entry_sobrenome_atendente.get()
        try:
            self.atendente_controller.alterar_atendente(nome, sobrenome, "codigo", cod_controle)
            messagebox.showinfo("Sucesso", "Atendente atualizado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar atendente: {e}")

    def deletar_atendente(self):
        cod_controle = self.entry_cod_atendente.get()
        try:
            self.atendente_controller.deletar_atendente(cod_controle)
            messagebox.showinfo("Sucesso", "Atendente deletado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar atendente: {e}")

    ## MÉTODOS PARA ATENDIMENTO ##
    def init_atendimento_widgets(self):
        # Widgets para o gerenciamento de atendimentos
        Label(self.frame_atendimento, text="Código do Atendimento:", font="Inter 10 bold").grid(row=0, column=0, padx=10, pady=5)
        self.entry_cod_atendimento = Entry(self.frame_atendimento)
        self.entry_cod_atendimento.grid(row=0, column=1, padx=10, pady=5)

        Button(self.frame_atendimento, text="Buscar", command=self.buscar_atendimento).grid(row=0, column=2, padx=10, pady=5)
        Button(self.frame_atendimento, text="Deletar", command=self.deletar_atendimento).grid(row=0, column=3, padx=10, pady=5)

    def buscar_atendimento(self):
        cod_atendimento = self.entry_cod_atendimento.get()
        try:
            atendimento = self.atendimento_controller.buscar_atendimento_por_codigo(cod_atendimento)
            if atendimento:
                messagebox.showinfo("Atendimento encontrado", f"Atendimento encontrado: {atendimento}")
            else:
                messagebox.showinfo("Atendimento não encontrado", "Nenhum atendimento encontrado com o código fornecido.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar atendimento: {e}")

    def deletar_atendimento(self):
        cod_atendimento = self.entry_cod_atendimento.get()
        try:
            self.atendimento_controller.deletar_atendimento(cod_atendimento)
            messagebox.showinfo("Sucesso", "Atendimento deletado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar atendimento: {e}")
