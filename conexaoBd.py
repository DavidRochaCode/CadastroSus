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
        cur.execute(exame)
        cur.execute(clinica)
        cur.execute(faz_exame)
        cur.execute(encaminha_exames)
        cur.execute(medicamento)
        cur.execute(atendimento)
        cur.execute(paciente)
        cur.execute(frequencia_atendimento)
        cur.execute(atendente)
        cur.execute(consulta)
        cur.execute(marcacao_consulta)
        cur.execute(dados_cadastrais)
        conn.commit()
    criar_tabela()

    #INSERIR CODIGO SQL DA PAGINA INICIAL AQUI

    def alteraTabelaAtendente():
        cur.execute("INSERT INTO atendente(nome, sobrenome, COD_atendente) VALUES(%s,%s,%s);",('david','emmanoel',1772893))
        conn.commit()
   

    def cadastrarTabelaPaciente():
        print("iu")

    cadastrarTabelaPaciente()

    def consultarTabelaPaciente():
        print("oi")
    consultarTabelaPaciente()

    def alteraTabelaMedico():
        print("oi")
    alteraTabelaMedico()

    def cadastrarTabelaAtendimento():
        print("oi")
    cadastrarTabelaAtendimento()

    def consultarTabelaAtendimento():
        print("oi")
    consultarTabelaAtendimento()

    def cadastrarTabelaConsulta():
        print("oi")
    cadastrarTabelaConsulta()

    def consultarTabelaConsulta():
        print("oi")
    consultarTabelaConsulta()

    def alterartabelaConsulta():
        print("oi")
    alterartabelaConsulta()

    def deletarTabelaConsulta():
        print("oi")
    deletarTabelaConsulta()


    def cadastrarTabelaMedicamento():
        print("oi")
    cadastrarTabelaMedicamento()

    def consultarTabelaMedicamento():
        print("oi")
    consultarTabelaMedicamento()

    def alterartabelaMedicamento():
        print("oi")
    alterartabelaMedicamento()

    def deletarTabelaMedicamento():
        print("oi")
    deletarTabelaMedicamento()

    def encaminharExames():
        print("iu")
    encaminharExames()

    def examesEncaminhados():
        print("oi")
    examesEncaminhados()

    def examesConcluidos():
        print("oi")
    examesConcluidos()

    def clinicas():
        print("oi")
    clinicas()

# --------------------------------------------------------------
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()