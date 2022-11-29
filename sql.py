
medico = '''CREATE TABLE IF NOT EXISTS medico (
            CRM INT PRIMARY KEY NOT NULL,
            nome VARCHAR(20) NOT NULL,
            cod_controle INT NOT NULL,
            atuacao VARCHAR(30) NOT NULL)'''



paciente = '''CREATE TABLE IF NOT EXISTS paciente(
            nome VARCHAR(30) NOT NULL,
            sobrenome VARCHAR(50) NOT NULL,
            celular VARCHAR(30) NOT NULL,
            endereco VARCHAR(50) NOT NULL,
            CPF_paciente VARCHAR(11) PRIMARY KEY NOT NULL,
            cartao_sus VARCHAR(20) NOT NULL,
            prontuario VARCHAR(11) NOT NULL
            )'''

atendimento = '''CREATE TABLE IF NOT EXISTS atendimento(
                COD_atendimento INT PRIMARY KEY NOT NULL,
                data_atendimento DATE NOT NULL DEFAULT CURRENT_DATE,
                CPF_paciente VARCHAR(11) NOT NULL,
                CRM INT NOT NULL,
                FOREIGN KEY(CRM) REFERENCES medico(CRM) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY(CPF_paciente) REFERENCES paciente(CPF_paciente)ON UPDATE CASCADE ON DELETE CASCADE) '''


atendente = '''CREATE TABLE IF NOT EXISTS atendente(
                nome VARCHAR (25) NOT NULL,
                sobrenome VARCHAR(45) NOT NULL,
                COD_controle INT NOT NULL,
                COD_atendente INT PRIMARY KEY NOT NULL)'''


