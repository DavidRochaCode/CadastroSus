from tkinter import Frame, Label, Entry, Button
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class AtendenteView:
    def __init__(self, master, controller):
        logging.info("Inicializando a visualização do atendente.")
        self.controller = controller
        self.frame_atendente = Frame(master)
        self.frame_atendente.pack(expand=True, fill="both")
        self.carregar_dados()  # Carrega dados ao iniciar

    def carregar_dados(self):
        logging.info("Carregando dados do atendente para exibição.")
        for widget in self.frame_atendente.winfo_children():
            widget.destroy()

        Label(self.frame_atendente, text="Nome:", font="Inter 9 bold", fg="#0B033F").place(x=90, y=130)
        self.label_nome_bd = Label(self.frame_atendente, font="Inter 9 bold", fg="black")
        self.label_nome_bd.place(x=130, y=130)

        Label(self.frame_atendente, text="Código:", font="Inter 9 bold", fg="#0B033F").place(x=90, y=170)
        self.label_cod_bd = Label(self.frame_atendente, font="Inter 9 bold", fg="black")
        self.label_cod_bd.place(x=135, y=170)

        Button(self.frame_atendente, text="Alterar", width=10, font="Inter 8 bold", fg="white", bg="#0B033F", command=self.alterar_atendente).place(x=175, y=225)

        try:
            atendentes = self.controller.buscar_atendentes()
            if isinstance(atendentes, list) and len(atendentes) > 0:
                atendente = atendentes[0]
                if isinstance(atendente, dict) and 'nome' in atendente and 'sobrenome' in atendente and 'cod_atendente' in atendente:
                    self.label_nome_bd.config(text=f"{atendente['nome']} {atendente['sobrenome']}")
                    self.label_cod_bd.config(text=atendente['cod_atendente'])
                else:
                    logging.warning("Dados do atendente são inválidos.")
                    self.label_nome_bd.config(text="Dados inválidos")
                    self.label_cod_bd.config(text="Dados inválidos")
            else:
                logging.info("Nenhum atendente encontrado.")
                self.label_nome_bd.config(text="Não encontrado")
                self.label_cod_bd.config(text="Não encontrado")
        except Exception as e:
            logging.error("Erro ao carregar dados do atendente: %s", e)

    def alterar_atendente(self):
        logging.info("Usuário iniciou alteração de dados do atendente.")
        for widget in self.frame_atendente.winfo_children():
            widget.destroy()

        Label(self.frame_atendente, text="Nome:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=30)
        entry_nome = Entry(self.frame_atendente, width=35)
        entry_nome.place(x=15, y=60)

        Label(self.frame_atendente, text="Sobrenome:", font="Inter 10 bold", fg="#0B033F").place(x=10, y=90)
        entry_sobrenome = Entry(self.frame_atendente, width=35)
        entry_sobrenome.place(x=15, y=120)

        Label(self.frame_atendente, text="Código:", font="Inter 10 bold", fg="#0B033F").place(x=15, y=160)
        entry_codigo = Entry(self.frame_atendente, width=35)
        entry_codigo.place(x=15, y=190)

        Button(self.frame_atendente, text="Salvar", width=10, font="Inter 8 bold", fg="white", bg="#0B033F", command=lambda: self.salvar_alteracoes(entry_nome.get(), entry_sobrenome.get(), entry_codigo.get())).place(x=85, y=250)

    def salvar_alteracoes(self, nome, sobrenome, codigo):
        logging.info("Salvando alterações do atendente: %s %s, Código: %s", nome, sobrenome, codigo)
        try:
            self.controller.alterar_atendente(nome, sobrenome, codigo, 12345)
            logging.info("Alterações salvas com sucesso.")
        except Exception as e:
            logging.error("Erro ao salvar alterações do atendente: %s", e)
        
        for widget in self.frame_atendente.winfo_children():
            widget.destroy()
        self.carregar_dados()
