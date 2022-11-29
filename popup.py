from tkinter import *
from tkinter import ttk
import psycopg2
from sql import *



#configuracao

#-----------------------------------------------------------------------------------------------------
hostname = 'localhost'
database = 'projetoubs'
username = 'postgres'
pwd = 'alaska'
port_id = 5432
conn = None
cur = None
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)
         
    cur = conn.cursor()

    #fim da configuracao


     #--------criar tabela------------#

    def criar_tabela():
        cur.execute(medico)
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



    """def popAtendenteAlterar():

        def alteraTabelaAtendente():
            cur.execute("UPDATE atendente SET nome = '{0}', sobrenome = '{1}', COD_atendente = {2} WHERE COD_controle = 12345;".format(entry_nome_atendente.get(), entry_sobrenome_atendente.get(), entry_codigo_atendente.get()))
            conn.commit()
            label_nome_bd.config(text = pegarNome())
            label_cod_atendente_bd.config(text=pegarCodigo())
           
    
        
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
                            
                                ).place(x = 85, y = 250)"""

    """def popPacienteConsulta():
        
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

        #geometria da janela
        tela_paciente.geometry("%dx%d+%d+%d" %(largura_resolucao,altura_resolucao,posicaoX,posicaoY))"""

        

    """def popMedicoAlterar():
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

        label_nome_atendente = Label(tela_medico,
                            text = "Nome:",
                            font = "Inter 10 bold",
                            fg = "#0B033F",
                            ).place(x = 10, y = 20)

        entry_nome_atendente = Entry(tela_medico, width = 35).place(x = 15, y = 50)


        label_crm_medico = Label(tela_medico,
                            text = "CRM:",
                            font = "Inter 10 bold",
                            fg = "#0B033F",
                            ).place(x = 15, y = 90)

        entry_crm_medico = Entry(tela_medico, width = 35).place(x = 15, y = 120)


        label_atuacao_medico = Label(tela_medico,
                            text = "Atuação:",
                            font = "Inter 10 bold",
                            fg = "#0B033F",
                            ).place(x = 15, y = 160)

        lista_tabelas = ["Pediatria", "Clínica Geral"]

        comboBox_tabelas = ttk.Combobox(tela_medico, values = lista_tabelas, justify = CENTER, font = "Inter 9 bold", width = 27)
        comboBox_tabelas.set("Secionar atuação")
        comboBox_tabelas.place(x = 15, y = 190)
            

        btn_medico = Button(tela_medico,
                                text = "Cadastrar",
                                width = 10,
                                font = "Inter 8 bold",
                                fg = "white",
                                bg = "#0B033F",
                                ).place(x = 85, y = 250)"""

    """def popAtendimentoConsultar():
        tela_atendimento = Toplevel()
        tela_atendimento.title("Cadastrar")
        tela_atendimento.resizable(False,False)
        tela_atendimento.grab_set()
        
        #resolução da tela
        largura_resolucao = 300
        altura_resolucao = 300
        largura_tela = tela_atendimento.winfo_screenwidth()
        altura_tela = tela_atendimento.winfo_screenheight()

        #posição da janela(centralizar)
        posicaoX = (largura_tela/2) - (largura_resolucao/2)
        posicaoY = (altura_tela/2) - (altura_resolucao/2)

        #geometria da janela
        tela_atendimento.geometry("%dx%d+%d+%d" %(largura_resolucao,altura_resolucao,posicaoX,posicaoY))"""

        
    


   
# --------------------------------------------------------------
except Exception as error:
    print(error)
