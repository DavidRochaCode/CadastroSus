import logging
from fastapi import FastAPI, HTTPException
from app.controllers import enfermeira_controller
from app.database.database_factory import DatabaseFactory

# Importar Modelos e Controladores
from app.models.atendente_model import AtendenteModel
from app.controllers.atendente_controller import AtendenteController

from app.models.medico_model import MedicoModel
from app.controllers.medico_controller import MedicoController

from app.models.paciente_model import PacienteModel
from app.controllers.paciente_controller import PacienteController

from app.models.atendimento_model import AtendimentoModel
from app.controllers.atendimento_controller import AtendimentoController

from app.models.enfermeira_model import EnfermeiraModel
from app.controllers.enfermeira_controller import EnfermeiraController

# Inicializar FastAPI
app = FastAPI(title="Sistema de Gestão UBS", version="1.0")

# Inicializar banco de dados
db = DatabaseFactory.create_database(
    db_type='postgresql',
    hostname='localhost',
    database='projetoubs',
    username='postgres',
    pwd='postgres',
    port_id=5432
)

# Configurar Modelos e Controladores
# Atendente
atendente_model = AtendenteModel(db)
atendente_model.criar_tabela()
atendente_controller = AtendenteController(atendente_model)

# Médico
medico_model = MedicoModel(db)
medico_model.criar_tabela()
medico_controller = MedicoController(medico_model)

# Paciente
paciente_model = PacienteModel(db)
paciente_model.criar_tabela()
paciente_controller = PacienteController(paciente_model)

# Atendimento
atendimento_model = AtendimentoModel(db)
atendimento_model.criar_tabela()
atendimento_controller = AtendimentoController(atendimento_model)

# Enfermeira
enfermeira_model = EnfermeiraModel(db)
enfermeira_model.criar_tabela()
enfermeira_controller = EnfermeiraController(enfermeira_model)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Sistema de Gestão UBS"}

# Rotas para Atendente
@app.get("/atendentes")
def get_atendentes():
    try:
        atendentes = atendente_controller.buscar_atendentes()
        return {"data": atendentes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/atendentes")
def create_atendente(nome: str, sobrenome: str, cod_atendente: int):
    try:
        resultado = atendente_controller.inserir_atendente(nome, sobrenome, cod_atendente)
        if resultado["status"] == "error":
            raise HTTPException(status_code=400, detail=resultado["message"])
        return {"message": resultado["message"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/atendentes/{cod_atendente}")
def update_atendente(cod_atendente: int, nome: str, sobrenome: str):
    try:
        resultado = atendente_controller.alterar_atendente(nome, sobrenome, cod_atendente)
        if resultado["status"] == "error":
            raise HTTPException(status_code=404, detail=resultado["message"])
        return {"message": resultado["message"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/atendentes/{cod_atendente}")
def delete_atendente(cod_atendente: int):
    try:
        resultado = atendente_controller.deletar_atendente(cod_atendente)
        if resultado["status"] == "error":
            raise HTTPException(status_code=404, detail=resultado["message"])
        return {"message": resultado["message"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Rotas para Médico
@app.post("/medicos")
def create_medico(crm: int, nome: str, atuacao: str):
    try:
        resultado = medico_controller.inserir_medico(crm, nome, atuacao)
        if resultado["status"] == "error":
            raise HTTPException(status_code=400, detail=resultado["message"])
        return {"message": "Médico inserido com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/medicos/{crm}")
def get_medico(crm: int):
    try:
        medico = medico_controller.buscar_medico_por_crm(crm)
        return {"data": medico}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/medicos")
def get_todos_medicos():
    try:
        medicos = medico_controller.buscar_todos_medicos()
        return {"data": medicos}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/medicos/{crm}")
def update_medico(crm: int, nome: str, atuacao: str):
    try:
        resultado = medico_controller.atualizar_medico(crm, nome, atuacao)
        if resultado["status"] == "error":
            raise HTTPException(status_code=404, detail=resultado["message"])
        return {"message": resultado["message"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/medicos/{crm}")
def delete_medico(crm: int):
    try:
        resultado = medico_controller.deletar_medico(crm)
        if resultado["status"] == "error":
            raise HTTPException(status_code=404, detail=resultado["message"])
        return {"message": "Médico deletado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Rotas para Paciente
@app.post("/pacientes")
def create_paciente(nome: str, sobrenome: str, cpf: str, cartao_sus: str, endereco: str, celular: str, prontuario: int):
    try:
        resultado = paciente_controller.inserir_paciente(nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario)
        if resultado["status"] == "error":
            raise HTTPException(status_code=400, detail=resultado["message"])
        return {"message": resultado["message"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/pacientes/{cpf}")
def get_paciente(cpf: str):
    try:
        paciente = paciente_controller.buscar_paciente(cpf)
        if paciente["status"] == "error":
            raise HTTPException(status_code=400, detail=paciente["message"])
        return {"data": paciente}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/pacientes/{cpf}")
def update_paciente(nome: str, sobrenome: str, cpf: str, cartao_sus: str, endereco: str, celular: str, prontuario: int):
    try:
        resultado = paciente_controller.alterar_paciente(nome, sobrenome, cpf, cartao_sus, endereco, celular, prontuario)
        if resultado["status"] == "error":
            raise HTTPException(status_code=404, detail=resultado["message"])
        return {"message": resultado["message"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/pacientes/{cpf}")
def delete_paciente(cpf: str):
    try:
        resultado = paciente_controller.deletar_paciente(cpf)
        if resultado["status"] == "error":
            raise HTTPException(status_code=404, detail=resultado["message"])
        return {"message": resultado["message"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Rotas para Atendimento
@app.post("/atendimentos")
def create_atendimento(cod_atendimento: int, cpf_paciente: str, crm: int):
    try:
        resultado = atendimento_controller.inserir_atendimento(cod_atendimento, cpf_paciente, crm)
        if resultado["status"] == "error":
            raise HTTPException(status_code=404, detail=resultado["message"])
        return {"message": resultado["message"]}
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/atendimentos/{cod_atendimento}")
def get_atendimento(cod_atendimento: int):
    try:
        atendimento = atendimento_controller.buscar_atendimento_por_codigo(cod_atendimento)
        if "status" in atendimento and atendimento["status"] == "error":
            raise HTTPException(status_code=404, detail=atendimento["message"])
        return {"data": atendimento}
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/atendimentos/{cod_atendimento}")
def delete_atendimento(cod_atendimento: int):
    try:
        resultado =  atendimento_controller.deletar_atendimento(cod_atendimento)
        if resultado["status"] == "error":
            raise HTTPException(status_code=404, detail=resultado["message"])
        return {"message": resultado["message"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/enfermeiras")
def get_enfermeiras():
    try:
        enfermeiras = enfermeira_controller.buscar_todas_enfermeiras()
        return {"data": enfermeiras}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/enfermeiras")
def create_enfermeira(nome: str, setor:str):
    try:
        enfermeira_controller.inserir_enfermeira(nome, setor)
        return {"message": "Enfermeira criada com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/enfermeiras")
def deletar_enfermeira(codigo):
        logging.info("Deletando enfermeira com código: %s", codigo)
        try:
            resultado = enfermeira_controller.deletar_enfermeira(codigo)
            if resultado["status"] == "error":
                raise HTTPException(status_code=404, detail=resultado["message"])
            logging.info("Enfermeira deletada com sucesso.")
            return {"message": resultado["message"]}
        except Exception as e:
            logging.error("Erro ao deletar enfermeira: %s", e)
            raise
        
@app.put("/enfermeiras/{codigo}")
def update_enfermeira(codigo: int, nome: str, setor: str):
    try:
        resultado = enfermeira_controller.atualizar_enfermeira(codigo, nome, setor)
        if resultado["status"] == "error":
            raise HTTPException(status_code=404, detail=resultado["message"])
        return {"message": resultado["message"]}
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.on_event("shutdown")
def shutdown_event():
    db.close()
