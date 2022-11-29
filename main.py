


from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
from turtle import st

from setuptools import Command
from popup import *
from sql import *
import psycopg2

# configuracao do banco de dado

# -----------------------------------------------------------------------------------------------------
hostname = 'localhost'
database = 'projetoubs'
username = 'postgres'
pwd = 'alaska'
port_id = 5432
conn = None
cur = None
try:
    
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    cur = conn.cursor()

    # fim da configuracao

    #--------criar tabela------------#


    def criar_tabela():
        cur.execute(medico)
        #cur.execute(exame)
        #cur.execute(clinica)
        #cur.execute(faz_exame)
        #cur.execute(encaminha_exames)
        #cur.execute(medicamento)
        cur.execute(atendimento)
        cur.execute(paciente)
        #cur.execute(frequencia_atendimento)
        cur.execute(atendente)
        #cur.execute(consulta)
        #cur.execute(marcacao_consulta)
        #cur.execute(dados_cadastrais)
        conn.commit()
    criar_tabela()


    tela = Tk()
    tela.title("UBS Garanhuns")
    tela.resizable(False, False)


    # resolução da tela

    largura_resolucao = 542
    altura_resolucao = 460
    largura_tela = tela.winfo_screenwidth()
    altura_tela = tela.winfo_screenheight()

    # posição da janela(centralizar)
    posicaoX = (largura_tela/2) - (largura_resolucao/2)
    posicaoY = (altura_tela/2) - (altura_resolucao/2)

    # geometria da janela
    tela.geometry("%dx%d+%d+%d" %
                (largura_resolucao, altura_resolucao, posicaoX, posicaoY))

    # elementos do header
    header_Frame = Frame(tela, width=largura_resolucao, height=85, bg="#0B033F")
    header_Frame.place(x=0, y=0)

    logo_garanhuns = PhotoImage(file="assets/brasao.png")
    labelImagem = Label(header_Frame, image=logo_garanhuns,
                        bg="#0B033F").place(x=30, y=5)

    label_ubs = Label(header_Frame,
                    text="UBS",
                    font="Inter 32 italic bold underline",
                    fg="white",
                    bg="#0B033F"
                    ).place(x=150, y=18)

    label_garanhuns = Label(header_Frame,
                            text="Garanhuns",
                            font="Inter 25",
                            fg="white",
                            bg="#0B033F"
                            ).place(x=253, y=28)


    # elementos do body

    aba_pai = ttk.Notebook(tela, width=430, height=315)
    aba_pai.place(x=50, y=85)

    #tb_medicamento = Frame(aba_pai)
    tb_medico = Frame(aba_pai)
    tb_atendimento = Frame(aba_pai)
    tb_Paciente = Frame(aba_pai)
    tb_atendente = Frame(aba_pai)

    aba_pai.add(tb_atendente, text="Atendente")
    aba_pai.add(tb_Paciente, text="Paciente")
    aba_pai.add(tb_medico, text="Médico")
    aba_pai.add(tb_atendimento, text="Atendimento")
    #aba_pai.add(tb_medicamento, text="Medicamento")


    # TABELA ATENDENTE-------------------------------------------------------------

    #popup da atendente---------------------------------------------------------------------
    def popAtendenteAlterar():

        def alteraTabelaAtendente():
            cur.execute("UPDATE atendente SET nome = '{0}', sobrenome = '{1}', COD_atendente = {2} WHERE COD_controle = 12345;".format(entry_nome_atendente.get(), entry_sobrenome_atendente.get(), entry_codigo_atendente.get()))
            conn.commit()
            label_nome_bd.config(text = pegarNome())
            label_cod_atendente_bd.config(text=pegarCodigo())
            tela_atendente.destroy()
           
        tela_atendente = Toplevel()
        tela_atendente.title("Cadastrar Atendente")
        tela_atendente.resizable(False,False)
        tela_atendente.grab_set()

        
        #resolução da tela
        largura_resolucao = 245
        altura_resolucao = 300
        largura_tela = tela_atendente.winfo_screenwidth()
        altura_tela = tela_atendente.winfo_screenheight()

        #posição da janela(centralizar)
        posicaoX = (largura_tela/2) - (largura_resolucao/2)
        posicaoY = (altura_tela/2) - (altura_resolucao/2)

        #geometria da janela
        tela_atendente.geometry("%dx%d+%d+%d" %(largura_resolucao,altura_resolucao,posicaoX,posicaoY))


        label_nome_atendente = Label(tela_atendente,
                            text = "Nome:",
                            font = "Inter 10 bold",
                            fg = "#0B033F"
                            ).place(x = 10, y = 30)

        entry_nome_atendente = Entry(tela_atendente, width = 35)
        entry_nome_atendente.place(x = 15, y = 60)

        label_sobrenome_atendente = Label(tela_atendente,
                            text = "Sobrenome:",
                            font = "Inter 10 bold",
                            fg = "#0B033F",
                            ).place(x = 10, y = 90)

        entry_sobrenome_atendente = Entry(tela_atendente, width = 35)
        entry_sobrenome_atendente.place(x = 15, y = 120)

        label_codigo_atendente = Label(tela_atendente,
                            text = "Código:",
                            font = "Inter 10 bold",
                            fg = "#0B033F").place(x = 15, y = 160)
        entry_codigo_atendente = Entry(tela_atendente, width= 35)
        entry_codigo_atendente.place(x = 15, y = 190)
        btn_atendente = Button(tela_atendente,
                                text = "Cadastrar",
                                width = 10,
                                font = "Inter 8 bold",
                                fg = "white",
                                bg = "#0B033F",
                                command= alteraTabelaAtendente
                            
                                ).place(x = 85, y = 250)

# fim do popup da atendente--------------------------------------------

# Pagina inicial atendente----------------------------------------------------------------
    frame_atendente = Frame(tb_atendente,
                            width=280,
                            height=240,
                            highlightbackground="grey",
                            highlightthickness=3
                            ).place(x=70, y=25)
    icon_atendente = PhotoImage(file="assets/user.png")
    labelImagem = Label(tb_atendente, image=icon_atendente).place(x=175, y=35)

    label_nome_atendente = Label(tb_atendente,
                                text="Nome:",
                                font="Inter 9 bold",
                                fg="#0B033F",
                                ).place(x=90, y=130)

    #codigo pega nome e sobrenome da tabela atendente                             
    def pegarNome():
        cur.execute("SELECT * FROM atendente")
        for record in cur.fetchall():
            nome = f"{record[0]} {record[1]}"
        return nome
   
    label_nome_bd = Label(tb_atendente,
                                text=pegarNome(),
                                font="Inter 9 bold",
                                fg="black",
                                )
    label_nome_bd.place(x = 130, y = 130)
    label_cod_atendente = Label(tb_atendente,
                                text="Código:",
                                font="Inter 9 bold",
                                fg="#0B033F",
                                ).place(x=90, y=170)

    #codigo pega codigo da tabela atendente                            
    def pegarCodigo():
        cur.execute("SELECT * FROM atendente")
        for record in cur.fetchall():
            codigo = record[3]
        return codigo

    label_cod_atendente_bd = Label(tb_atendente,
                                text=pegarCodigo(),
                                font="Inter 9 bold",
                                fg="black",
                                )
    label_cod_atendente_bd.place(x=135, y=170)
    button_alterar_atendente = Button(tb_atendente,
                                    text="Alterar",
                                    width=10,
                                    font="Inter 8 bold",
                                    fg="white",
                                    bg="#0B033F",
                                    command=popAtendenteAlterar

                                    ).place(x=175, y=225)
    # fim da página inicial atendente

    #FIM DA TABELA ATENDENTE------------------------------------------------------------
    

    # TABELA MÉDICO----------------------------------------------------------------------
    def obterInformacao(n):
            cur.execute(f"SELECT * FROM medico")
            for record in cur.fetchall():
                info = record[n]
            return info

    def popMedicoAlterar():

        

        def inserirInformacao():
           cur.execute(f"UPDATE medico SET crm = {entry_crm_medico_popup.get()}, nome = '{entry_nome_medico_popup.get()}', atuacao = '{comboBox_tabelas.get()}' WHERE cod_controle = 1234;")
           conn.commit()
           label_nome_medico_show.config(text =obterInformacao(1))
           label_crm_medico_show.config(text=obterInformacao(0))
           label_atuacao_medico_show.config(text = obterInformacao(3))
           tela_medico.destroy()

    

        tela_medico = Toplevel()
        tela_medico.title("Cadastrar")
        tela_medico.resizable(False,False)
        tela_medico.grab_set()
        
        #resolução da tela
        largura_resolucao = 245
        altura_resolucao = 300
        largura_tela = tela_medico.winfo_screenwidth()
        altura_tela = tela_medico.winfo_screenheight()

        #posição da janela(centralizar)
        posicaoX = (largura_tela/2) - (largura_resolucao/2)
        posicaoY = (altura_tela/2) - (altura_resolucao/2)

        #geometria da janela
        tela_medico.geometry("%dx%d+%d+%d" %(largura_resolucao,altura_resolucao,posicaoX,posicaoY))

        label_nome_medico_popup = Label(tela_medico,
                            text = "Nome:",
                            font = "Inter 10 bold",
                            fg = "#0B033F",
                            ).place(x = 10, y = 20)

        entry_nome_medico_popup = Entry(tela_medico, width = 35)
        entry_nome_medico_popup.place(x = 15, y = 50)


        label_crm_medico_popup = Label(tela_medico,
                            text = "CRM:",
                            font = "Inter 10 bold",
                            fg = "#0B033F",
                            ).place(x = 15, y = 90)

        entry_crm_medico_popup = Entry(tela_medico, width = 35)
        entry_crm_medico_popup.place(x = 15, y = 120)

        label_atuacao_medico = Label(tela_medico,
                            text = "Atuação:",
                            font = "Inter 10 bold",
                            fg = "#0B033F",
                            ).place(x = 15, y = 160)

        lista_atuacao = ["Pediatria", "Clínica Geral"]

        comboBox_tabelas = ttk.Combobox(tela_medico, values = lista_atuacao, justify = CENTER, font = "Inter 9 bold", width = 27)
        comboBox_tabelas.set("Secionar atuação")
        comboBox_tabelas.place(x = 15, y = 190)
            

        btn_medico = Button(tela_medico,
                                text = "Cadastrar",
                                width = 10,
                                font = "Inter 8 bold",
                                fg = "white",
                                bg = "#0B033F",
                                command=inserirInformacao
                                ).place(x = 85, y = 250),
                                

 #Fim popup médico

 # página inicial médico

    frame_medico = Frame(tb_medico,
                        width=280,
                        height=240,
                        highlightbackground="grey",
                        highlightthickness=3
                        ).place(x=70, y=25)
    icon_medico = PhotoImage(file="assets/user.png")
    labelImagem = Label(tb_medico, image=icon_medico).place(x=175, y=35)

    label_nome_medico = Label(tb_medico,
                            text="Nome:",
                            font="Inter 9 bold",
                            fg="#0B033F",
                            )
    label_nome_medico.place(x=90, y=120)
    label_nome_medico_show = Label(tb_medico,text = f"{obterInformacao(1)}",font="Inter 9 bold",fg="black",)
    label_nome_medico_show.place(x = 130 , y = 120)


    label_crm_medico = Label(tb_medico,
                            text="CRM:",
                            font="Inter 9 bold",
                            fg="#0B033F",
                            ).place(x=90, y=145)
    label_crm_medico_show = Label(tb_medico, text=f"{obterInformacao(0)}",  font="Inter 9 bold", fg="black")
    label_crm_medico_show.place(x=125,y = 145 )

    label_atuacao_medico = Label(tb_medico,
                                text="Atuação:",
                                font="Inter 9 bold",
                                fg="#0B033F",
                                ).place(x=90, y=170)
    label_atuacao_medico_show = Label(tb_medico,text=f"{obterInformacao(3)}",  font="Inter 9 bold", fg="black")
    label_atuacao_medico_show.place(x = 145, y = 170)

    button_alterar_medico = Button(tb_medico,
                                text="Alterar",
                                width=10,
                                font="Inter 8 bold",
                                fg="white",
                                bg="#0B033F",
                                command=popMedicoAlterar


                                ).place(x=175, y=225)

   

    # TABELA PACIENTE -----------------------------------------------------------------------------

    # -cadastro

    def cadastrarPaciente():
        cur.execute("INSERT INTO paciente(nome,sobrenome,CPF_paciente,cartao_sus,endereco,celular, prontuario) VALUES(%s,%s,%s,%s,%s,%s,%s);"
        ,(entry_nome_paciente.get(),
         entry_sobrenome_paciente.get(),
         entry_cpf_paciente.get(),
         entry_sus_paciente.get(),
         entry_endereco_paciente.get(),
         entry_telefone__paciente.get(),
         entry_prontuario_paciente.get()))
        conn.commit()
        entry_nome_paciente.delete(0,END)
        entry_sobrenome_paciente.delete(0,END)
        entry_cpf_paciente.delete(0,END)
        entry_sus_paciente.delete(0,END)
        entry_endereco_paciente.delete(0,END)
        entry_telefone__paciente.delete(0,END)
        entry_prontuario_paciente.delete(0,END)



    style = ttk.Style(tb_Paciente)
    style.configure('lefttab.TNotebook', tabposition='wn')

    aba_pai_paciente = ttk.Notebook(
        tb_Paciente, style='lefttab.TNotebook', width=330, height=280)

    tabela_cadastrar_paciente = Frame(aba_pai_paciente)
    tabela_consultar_paciente = Frame(aba_pai_paciente)

    aba_pai_paciente.add(tabela_cadastrar_paciente, text='Cadastrar')
    aba_pai_paciente.add(tabela_consultar_paciente, text='Consultar')

    aba_pai_paciente.place(x=15, y=25)

    label_nome_paciente = Label(tabela_cadastrar_paciente,
                                text="Nome completo*:",
                                font="inter 9 bold",
                                fg="#0B033F"
                                ).place(x=20, y=13)
    entry_nome_paciente = Entry(
        tabela_cadastrar_paciente, width=20)

    entry_nome_paciente.place(x=20, y=35)

    entry_sobrenome_paciente = Entry(
        tabela_cadastrar_paciente, width=20)
    
    entry_sobrenome_paciente.place(x=165, y=35)
    
    label_mensagem_nome = Label(tabela_cadastrar_paciente,
                                text="Nome",
                                font="Inter 6",

                                ).place(x=20, y=60)
    label_mensagem_sobrenome = Label(tabela_cadastrar_paciente,
                                    text="Sobrenome",
                                    font="Inter 6",

                                    ).place(x=165, y=60)

    label_cpf_paciente = Label(tabela_cadastrar_paciente,
                            text="CPF*:",
                            font="inter 9 bold",
                            fg="#0B033F"
                            ).place(x=20, y=80)
    entry_cpf_paciente = Entry(tabela_cadastrar_paciente,
                            width=20)
    entry_cpf_paciente.place(x=20, y=100)

    label_sus_paciente = Label(tabela_cadastrar_paciente,
                            text="Cartão do sus*:",
                            font="Inter 9 bold",
                            fg="#0B033F"
                            ).place(x=165, y=80)

    entry_sus_paciente = Entry(tabela_cadastrar_paciente,
                            width=20)
    entry_sus_paciente.place(x=165, y=100)

    label_endereco_paciente = Label(tabela_cadastrar_paciente,
                                    text="Endereço*:",
                                    font="Inter 9 bold",
                                    fg="#0B033F"
                                    ).place(x=20, y=130)

    entry_endereco_paciente = Entry(
        tabela_cadastrar_paciente, width=45)

    entry_endereco_paciente.place(x=20, y=150)

    label_telefone_paciente = Label(tabela_cadastrar_paciente,
                                    text="Celular:",
                                    font="Inter 9 bold",
                                    fg="#0B033F"

                                    ).place(x=20, y=180)
    entry_telefone__paciente = Entry(
        tabela_cadastrar_paciente, width=20)

    entry_telefone__paciente.place(x=20, y=200)

    label_prontuario_paciente = Label(tabela_cadastrar_paciente,
                                    text="N⁰ prontuário*:",
                                    font="Inter 9 bold",
                                    fg="#0B033F"
                                    ).place(x=165, y=180)

    entry_prontuario_paciente = Entry(
        tabela_cadastrar_paciente, width=20)

    entry_prontuario_paciente.place(x=165, y=200)

    button_cadastrar_paciente = Button(tabela_cadastrar_paciente,
                                    text="Cadastrar",
                                    font="Inter 8 bold",
                                    fg="white",
                                    bg="#0B033F",
                                    command=cadastrarPaciente

                                    ).place(x=132, y=240)

    # --consulta

    #--Popup do consultar paciente----------------------------------------------------------
    def popPacienteConsulta():
    
        def buscarNomePaciente():
            cur.execute(f"SELECT * FROM paciente WHERE cpf_paciente = '{entry_consultar_paciente.get()}'")
            for record in cur.fetchall():
                nome = f"{record[0]} {record[1]}"
            return nome

        def buscarCpfPaciente():
            cur.execute(f"SELECT * FROM paciente WHERE cpf_paciente = '{entry_consultar_paciente.get()}'")
            for record in cur.fetchall():
                cpf = record[4]
            return cpf
            
        def buscarSusPaciente():
            cur.execute(f"SELECT * FROM paciente WHERE cpf_paciente = '{entry_consultar_paciente.get()}'")
            for record in cur.fetchall():
                sus = record[5]
            return sus

        def buscarEnderecoPaciente():
            cur.execute(f"SELECT * FROM paciente WHERE cpf_paciente = '{entry_consultar_paciente.get()}'")
            for record in cur.fetchall():
                endereco = record[3]
            return endereco

        def buscarProntuarioPaciente():
            cur.execute(f"SELECT * FROM paciente WHERE cpf_paciente = '{entry_consultar_paciente.get()}'")
            for record in cur.fetchall():
                prontuario = record[6]
            return prontuario
        
        def button_deletar_paciente():
            cur.execute(f"DELETE FROM paciente WHERE cpf_paciente = '{entry_consultar_paciente.get()}'")
            conn.commit()
            tela_paciente.destroy()
            

        def popup_button_alterar_paciente():

                #pegar as informaçãoes já para deixar setado nos entrys
                def pegarInfo(n):
                    cur.execute(f"SELECT * FROM paciente WHERE cpf_paciente = '{entry_consultar_paciente.get()}'")
                    for record in cur.fetchall():
                        codigo = record[n]
                    return codigo
                

                tela_alterar_paciente = Toplevel()
                tela_alterar_paciente.title("Alterar")
                tela_alterar_paciente.resizable(False,False)
                tela_alterar_paciente.grab_set()
                
                #resolução da tela
                largura_resolucao = 330
                altura_resolucao = 300
                largura_tela = tela_alterar_paciente.winfo_screenwidth()
                altura_tela = tela_alterar_paciente.winfo_screenheight()

                #posição da janela(centralizar)
                posicaoX = (largura_tela/2) - (largura_resolucao/2)
                posicaoY = (altura_tela/2) - (altura_resolucao/2)

                tela_alterar_paciente.geometry("%dx%d+%d+%d" %(largura_resolucao,altura_resolucao,posicaoX,posicaoY)) 

                label_nome_paciente = Label(tela_alterar_paciente,
                                text="Nome completo*:",
                                font="inter 9 bold",
                                fg="#0B033F"
                                ).place(x=20, y=13)
                entry_nome_paciente_mudar = Entry(tela_alterar_paciente, width=20)
                entry_nome_paciente_mudar.insert(0, pegarInfo(0))
                entry_nome_paciente_mudar.place(x=20, y=35)

                entry_sobrenome_paciente_mudar = Entry(tela_alterar_paciente, width=20)
                entry_sobrenome_paciente_mudar.insert(0,pegarInfo(1))
                entry_sobrenome_paciente_mudar.place(x=165, y=35)
                
                label_mensagem_nome = Label(tela_alterar_paciente,
                                            text="Nome",
                                            font="Inter 6",

                                            ).place(x=20, y=60)
                label_mensagem_sobrenome = Label(tela_alterar_paciente,
                                                text="Sobrenome",
                                                font="Inter 6",

                                                ).place(x=165, y=60)

                label_cpf_paciente = Label(tela_alterar_paciente,
                                        text="CPF*:",
                                        font="inter 9 bold",
                                        fg="#0B033F"
                                        ).place(x=20, y=80)
                entry_cpf_paciente_mudar = Entry(tela_alterar_paciente,width=20)
                entry_cpf_paciente_mudar.insert(0,pegarInfo(4))
                entry_cpf_paciente_mudar.place(x=20, y=100)

                label_sus_paciente = Label(tela_alterar_paciente,
                                        text="Cartão do sus*:",
                                        font="Inter 9 bold",
                                        fg="#0B033F"
                                        ).place(x=165, y=80)

                entry_sus_paciente_mudar = Entry(tela_alterar_paciente,width=20)
                entry_sus_paciente_mudar.insert(0,pegarInfo(5))
                entry_sus_paciente_mudar.place(x=165, y=100)

                label_endereco_paciente = Label(tela_alterar_paciente,
                                                text="Endereço*:",
                                                font="Inter 9 bold",
                                                fg="#0B033F"
                                                ).place(x=20, y=130)

                entry_endereco_paciente_mudar = Entry(tela_alterar_paciente, width=45)
                entry_endereco_paciente_mudar.insert(0,pegarInfo(3))
                entry_endereco_paciente_mudar.place(x=20, y=150)
              

                label_telefone_paciente = Label(tela_alterar_paciente,
                                                text="Celular:",
                                                font="Inter 9 bold",
                                                fg="#0B033F"

                                                ).place(x=20, y=180)
                entry_telefone_paciente_mudar = Entry(tela_alterar_paciente, width=20)
                entry_telefone_paciente_mudar.insert(0,pegarInfo(2))
                entry_telefone_paciente_mudar.place(x=20, y=200)

                label_prontuario_paciente = Label(tela_alterar_paciente,
                                                text="N⁰ prontuário*:",
                                                font="Inter 9 bold",
                                                fg="#0B033F"
                                                ).place(x=165, y=180)

                entry_prontuario_paciente_mudar = Entry(tela_alterar_paciente, width=20)
                entry_prontuario_paciente_mudar.insert(0,pegarInfo(6))
                entry_prontuario_paciente_mudar.place(x=165, y=200)


                def alterarPaciente():
                    cur.execute("UPDATE paciente SET nome = '{0}', sobrenome = '{1}', celular = '{2}', endereco = '{3}', cpf_paciente = '{4}', cartao_sus = '{5}', prontuario = '{6}' WHERE cpf_paciente = '{7}';".format(
                    entry_nome_paciente_mudar.get(),
                    entry_sobrenome_paciente_mudar.get(),
                    entry_telefone_paciente_mudar.get(),
                    entry_endereco_paciente_mudar.get(),
                    entry_cpf_paciente_mudar.get(),
                    entry_sus_paciente_mudar.get(),
                    entry_prontuario_paciente_mudar.get(),
                    entry_consultar_paciente.get()
                    ))
                    label_nome_paciente_popup_show.config(text=buscarNomePaciente())
                    label_cpf_paciente_popup_show.config(text=buscarCpfPaciente())
                    label_sus_paciente_popup_show.config(text=buscarSusPaciente())
                    label_endereco_paciente_popup_show.config(text=buscarEnderecoPaciente())
                    label_prontuario_paciente_popup_show.config(text=buscarProntuarioPaciente())
                    tela_alterar_paciente.destroy()
                    conn.commit()

                button_cadastrar_paciente = Button(tela_alterar_paciente,
                                                text="Alterar",
                                                font="Inter 8 bold",
                                                fg="white",
                                                bg="#0B033F",
                                                command= alterarPaciente
                                                ).place(x=132, y=240)
               

        tela_paciente = Toplevel()
        tela_paciente.title("Cadastrar")
        tela_paciente.resizable(False,False)
        tela_paciente.grab_set()
        
        #resolução da tela
        largura_resolucao = 300
        altura_resolucao = 300
        largura_tela = tela_paciente.winfo_screenwidth()
        altura_tela = tela_paciente.winfo_screenheight()

        #posição da janela(centralizar)
        posicaoX = (largura_tela/2) - (largura_resolucao/2)
        posicaoY = (altura_tela/2) - (altura_resolucao/2)

        tela_paciente.geometry("%dx%d+%d+%d" %(largura_resolucao,altura_resolucao,posicaoX,posicaoY))


        label_nome_paciente_popup = Label(tela_paciente, text = "Nome:",font="Inter 9 bold", fg="#0B033F")
        label_nome_paciente_popup.place(x = 15, y = 15)

        label_nome_paciente_popup_show = Label(tela_paciente, text = buscarNomePaciente(),font="Inter 9 bold", fg="black")
        label_nome_paciente_popup_show.place(x = 60, y = 15 )

        label_cpf_paciente_popup = Label(tela_paciente, text = "CPF:",font="Inter 9 bold", fg="#0B033F")
        label_cpf_paciente_popup.place(x = 15, y = 40)

        label_cpf_paciente_popup_show = Label(tela_paciente,text = buscarCpfPaciente(),font="Inter 9 bold", fg="black")
        label_cpf_paciente_popup_show.place(x = 50, y = 40)

        label_sus_paciente_popup = Label(tela_paciente, text = "SUS:",font="Inter 9 bold", fg="#0B033F")
        label_sus_paciente_popup.place(x = 15, y = 65)

        label_sus_paciente_popup_show = Label(tela_paciente,text = buscarSusPaciente(),font="Inter 9 bold", fg="black")
        label_sus_paciente_popup_show.place(x = 50, y = 65 )

        label_endereco_paciente_popup = Label(tela_paciente, text = "Endereço:",font="Inter 9 bold", fg="#0B033F")
        label_endereco_paciente_popup.place(x = 15, y = 90)

        label_endereco_paciente_popup_show = Label(tela_paciente,text = buscarEnderecoPaciente(),font="Inter 9 bold", fg="black")
        label_endereco_paciente_popup_show.place(x = 75, y =90 )

        label_prontuario_paciente_popup = Label(tela_paciente, text = "Prontuário:",font="Inter 9 bold", fg="#0B033F")
        label_prontuario_paciente_popup.place(x = 15, y = 115)

        label_prontuario_paciente_popup_show = Label(tela_paciente, text = buscarProntuarioPaciente(),font="Inter 9 bold", fg="black")
        label_prontuario_paciente_popup_show.place(x = 85, y = 115)

        button_deletar_paciente = Button(tela_paciente,text="Deletar dados",width=20,font="Inter 8 bold",fg="white",bg="#0B033F", command=button_deletar_paciente )
        button_deletar_paciente.place(x = 70, y = 180)

        button_alterar_paciente = Button(tela_paciente,text="Alterar dados",width=20,font="Inter 8 bold",fg="white",bg="#0B033F", command=popup_button_alterar_paciente)
        button_alterar_paciente.place(x = 70, y = 215)

        #--Fim do popup do consultar paciente
    

    label_consultar_paciente = Label(tabela_consultar_paciente,
                                    text="CPF do paciente:",
                                    font="Inter 10 bold",
                                    fg="#0B033F",
                                    ).place(x=100, y=60)
    entry_consultar_paciente = Entry(tabela_consultar_paciente,
                                    bg="white"
                                    )
    entry_consultar_paciente.place(x=95, y=90)
    btn_consultar_paciente = Button(tabela_consultar_paciente,
                                    text="Consultar",
                                    width=10,
                                    font="Inter 8 bold",
                                    fg="white",
                                    bg="#0B033F",
                                    command=popPacienteConsulta
                                    ).place(x=120, y=130)
   

    # -tabela atendimento

    # cadastro

    
    def cadastrarInforatendimento():
            def buscarCPF():
                cur.execute(f"SELECT EXISTS(SELECT cpf_paciente FROM paciente WHERE cpf_paciente = '{entry_cpf_atendimento.get()}')")
                for i in cur.fetchall():
                    checar = i[0]
                return checar
            
            if buscarCPF():
                # print(buscarCPF())
                # print("existe")
                def obterCRM():
                    cur.execute("SELECT * FROM medico")
                    for record in cur.fetchall():
                        crm = record[0]
                    return crm
                cur.execute(f"INSERT INTO atendimento(cod_atendimento,cpf_paciente,crm) VALUES({entry_cod_atendimento.get()},{entry_cpf_atendimento.get()}, {obterCRM()})")
                conn.commit()
                entry_cpf_atendimento.delete(0,END)
                entry_cod_atendimento.delete(0,END)
                print(buscarCPF())
            else:
                entry_cpf_atendimento.delete(0,END)
                entry_cod_atendimento.delete(0,END)
                #criar tela de aviso
                tela_erro = Toplevel()
                tela_erro.resizable(False,False)
                tela_erro.title("Cadastrar")
                tela_erro.grab_set()
                tela_erro.configure(bg = "#0B033F")
                
                #resolução da tela
                largura_resolucao = 380
                altura_resolucao = 200
                largura_tela = tela_erro.winfo_screenwidth()
                altura_tela = tela_erro.winfo_screenheight()

                #posição da janela(centralizar)
                posicaoX = (largura_tela/2) - (largura_resolucao/2)
                posicaoY = (altura_tela/2) - (altura_resolucao/2)

                tela_erro.geometry("%dx%d+%d+%d" %(largura_resolucao,altura_resolucao,posicaoX,posicaoY))
                def fecharTela():
                    tela_erro.destroy()
                label_erro = Label(tela_erro, text = "Não há nenhum paciente cadastrado com esse CPF", bg = "#0B033F", fg = "white", font = "Inter 10 bold").place(x =25, y = 60)
                botao_erro = Button(tela_erro, text = "OK", bg = "white", fg = "#0B033F", font ="Inter 6 bold", width=10, command= fecharTela).place(x = 180, y = 150)
                
          
    
            


    style = ttk.Style(tb_atendimento)
    style.configure('lefttab.TNotebook', tabposition='wn')

    aba_pai_atendimento = ttk.Notebook(
        tb_atendimento, style='lefttab.TNotebook', width=330, height=280)

    tabela_cadastrar_atendimento = Frame(aba_pai_atendimento)
    tabela_consultar_atendimento = Frame(aba_pai_atendimento)

    aba_pai_atendimento.add(tabela_cadastrar_atendimento, text='Cadastrar')
    aba_pai_atendimento.add(tabela_consultar_atendimento, text='Consultar')

    aba_pai_atendimento.place(x=15, y=25)



    label_cpf_atendimento = Label(tabela_cadastrar_atendimento,
                                text="CPF:",
                                font="Inter 9 bold",
                                fg="#0B033F"
                                ).place(x=15, y=20)

    entry_cpf_atendimento = Entry(
        tabela_cadastrar_atendimento, width=35)
    entry_cpf_atendimento.place(x=15, y=45)


    label_cod_atendimento = Label(tabela_cadastrar_atendimento,
                                text="Código:",
                                font="Inter 9 bold",
                                fg="#0B033F"
                                ).place(x=15, y=80)

    entry_cod_atendimento = Entry(
        tabela_cadastrar_atendimento, width=35)
    entry_cod_atendimento.place(x=15, y=100)

    button_cadastrar_paciente = Button(tabela_cadastrar_atendimento,
                                    text="Cadastrar",
                                    font="Inter 8 bold",
                                    fg="white",
                                    bg="#0B033F",
                                    command=cadastrarInforatendimento

                                    ).place(x=100, y=140)

    # --consulta e deleter


    def popAtendimentoConsultar():
        def buscarCPF():
                cur.execute(f"SELECT EXISTS(SELECT cod_atendimento FROM atendimento WHERE cod_atendimento = '{entry_consultar_atendimento.get()}')")
                for i in cur.fetchall():
                    checar = i[0]
                return checar
        
        if buscarCPF():
            tela_atendimento = Toplevel()
            tela_atendimento.title("Cadastrar")
            tela_atendimento.resizable(False,False)
            tela_atendimento.grab_set()
            
            #resolução da tela
            largura_resolucao = 300
            altura_resolucao = 380
            largura_tela = tela_atendimento.winfo_screenwidth()
            altura_tela = tela_atendimento.winfo_screenheight()

            #posição da janela(centralizar)
            posicaoX = (largura_tela/2) - (largura_resolucao/2)
            posicaoY = (altura_tela/2) - (altura_resolucao/2)

            #geometria da janela
            tela_atendimento.geometry("%dx%d+%d+%d" %(largura_resolucao,altura_resolucao,posicaoX,posicaoY))


            #buscar informações na tabela atendimento

        
            def obterInformacaoAtendimento(n):
                        global informacoes
                        informacoes = ""
                        cur.execute(f"SELECT paciente.nome,paciente.sobrenome,paciente.celular,paciente.cartao_sus,to_char(atendimento.data_atendimento, 'DD/MM/YYYY'),\
                            atendimento.cod_atendimento,atendimento.cpf_paciente, medico.nome, medico.CRM, medico.atuacao\
                            FROM atendimento INNER JOIN paciente on paciente.cpf_paciente = atendimento.cpf_paciente \
                            INNER JOIN medico on atendimento.CRM = medico.CRM WHERE atendimento.cod_atendimento = {entry_consultar_atendimento.get()}"
                        )
                        for record in cur.fetchall():
                            
                            informacoes= record[n]
                        return informacoes

                    #deletar Tabela atendimento
            def deletarAtendimento():
                        cur.execute(f"DELETE FROM atendimento WHERE cod_atendimento = {entry_consultar_atendimento.get()}")
                        conn.commit()
                        tela_atendimento.destroy()
                    
                    
                        

            label_cod_atendimento = Label(tela_atendimento, text = "Código:",font="Inter 10 bold", fg="#0B033F" ).place(x = 15, y = 15)
            label_cod_atendimento_show = Label(tela_atendimento, text = obterInformacaoAtendimento(5),font="Inter 10 bold", fg="black")
            label_cod_atendimento_show.place(x = 70, y = 15)

            label_nome_atendimento = Label(tela_atendimento, text = "Nome:",font="Inter 10 bold", fg="#0B033F").place(x = 15, y = 45)
            label_nome_atendimento_show = Label(tela_atendimento, text = f"{obterInformacaoAtendimento(0)} {obterInformacaoAtendimento(1)}",font="Inter 10 bold", fg="black")
            label_nome_atendimento_show.place(x = 65, y = 45)


            label_cpf_paciente_atendimento = Label(tela_atendimento, text = "CPF:",font="Inter 10 bold", fg="#0B033F").place(x = 15, y = 75)
            label_cpf_paciente_atendimento_show = Label(tela_atendimento, text = obterInformacaoAtendimento(6),font="Inter 10 bold", fg="black")
            label_cpf_paciente_atendimento_show.place(x = 50, y = 75)


            label_sus_atendimento = Label(tela_atendimento, text = "SUS:",font="Inter 10 bold", fg="#0B033F").place(x = 15, y = 105 )
            label_sus_atendimento_show = Label(tela_atendimento, text = obterInformacaoAtendimento(3),font="Inter 10 bold", fg="black")
            label_sus_atendimento_show.place(x = 50, y = 105)


            label_contato_atendimento = Label(tela_atendimento, text = "Contato:",font="Inter 10 bold", fg="#0B033F").place(x = 15, y = 135)
            label_contato_atendimento_show = Label(tela_atendimento, text = obterInformacaoAtendimento(2),font="Inter 10 bold", fg="black")
            label_contato_atendimento_show.place(x = 70, y = 135)


            label_data_atendimento = Label(tela_atendimento, text = "Data:",font="Inter 10 bold", fg="#0B033F").place(x = 15, y = 165)
            label_data_atendimento_show = Label(tela_atendimento, text =obterInformacaoAtendimento(4),font="Inter 10 bold", fg="black")
            label_data_atendimento_show.place(x = 55, y = 165)

            label_medico_responsavel = Label(tela_atendimento, text = "Médico responsável:",font="Inter 10 bold", fg="#0B033F").place(x = 15, y = 195)
            label_medico_responsavel_show = Label(tela_atendimento, text = obterInformacaoAtendimento(7),font="Inter 10 bold", fg="black").place(x = 150, y = 195)

            label_crm_medico_reponsavel= Label(tela_atendimento, text = "CRM:",font="Inter 10 bold", fg="#0B033F").place(x = 15, y = 225)
            label_crm_medico_reponsavel_show = Label(tela_atendimento, text = obterInformacaoAtendimento(8),font="Inter 10 bold", fg="black").place(x = 50, y = 225)

            label_atuacao_medico_reponsavel = Label(tela_atendimento, text = "Atuação:",font="Inter 10 bold", fg="#0B033F").place(x = 15, y = 255)
            label_atuacao_medico_reponsavel_show = Label(tela_atendimento, text = obterInformacaoAtendimento(9),font="Inter 10 bold", fg="black").place(x = 75, y = 255)

                    

            button_atendimento = Button(tela_atendimento,  text="Deletar atendimento",font="Inter 8 bold",fg="white",bg="#0B033F", command=deletarAtendimento).place(x = 90, y = 320)
        else:
            entry_consultar_atendimento.delete(0,END)
            tela_erro_consultar = Toplevel()
            tela_erro_consultar.resizable(False,False)
            tela_erro_consultar.title("Cadastrar")
            tela_erro_consultar.grab_set()
            tela_erro_consultar.configure(bg = "#0B033F")
                
                #resolução da tela
            largura_resolucao = 410
            altura_resolucao = 200
            largura_tela = tela_erro_consultar.winfo_screenwidth()
            altura_tela = tela_erro_consultar.winfo_screenheight()

                #posição da janela(centralizar)
            posicaoX = (largura_tela/2) - (largura_resolucao/2)
            posicaoY = (altura_tela/2) - (altura_resolucao/2)

            tela_erro_consultar.geometry("%dx%d+%d+%d" %(largura_resolucao,altura_resolucao,posicaoX,posicaoY))
            def fecharTela():
                tela_erro_consultar.destroy()
            label_erro = Label(tela_erro_consultar, text = "Não há nenhum atendimento cadastrado com esse Código", bg = "#0B033F", fg = "white", font = "Inter 10 bold").place(x =15, y = 60)
            botao_erro = Button(tela_erro_consultar, text = "OK", bg = "white", fg = "#0B033F", font ="Inter 6 bold", width=10, command= fecharTela).place(x = 180, y = 150)

    label_consultar_atendimento = Label(tabela_consultar_atendimento,
                                        text="Código do atendimento:",
                                        font="Inter 10 bold",
                                        fg="#0B033F",
                                        ).place(x=80, y=60)
    entry_consultar_atendimento = Entry(tabela_consultar_atendimento,
                                        bg="white"
                                        )
    entry_consultar_atendimento.place(x=95, y=90)

    btn_consultar_atendimento = Button(tabela_consultar_atendimento,
                                    text="Consultar",
                                    width=10,
                                    font="Inter 8 bold",
                                    fg="white",
                                    bg="#0B033F",
                                    command=popAtendimentoConsultar
                                    ).place(x=115, y=130)

    # footer
    footer_Frame = Frame(tela, width=largura_resolucao, height=35, bg="#0B033F")
    footer_Frame.place(x=0, y=426)

    label_footer = Label(footer_Frame,
                        text="Endereço: R. Sebastião Paes de Melo, 581-601 - Heliópolis, Garanhuns - PE, 55298-520",
                        font="Inter 6 ",
                        fg="white",
                        bg="#0B033F"
                        ).place(x=10, y=9)

    tela.mainloop()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

    
