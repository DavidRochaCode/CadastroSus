# CadastroSus

Projeto de banco de dados de um Sistema de cadastro de pacientes na Unidade Básica de Saúde (SUS) 

Sistema desenvolvido como projeto final da diciplina de Banco de Dados.

Mini mundo do sistema: 

Em uma unidade básica de saúde ( UBS ), são atendidos pacientes distribuídos por regiões, desse modo:

Os pacientes, que possuem nome, sobrenome e CPF, são atendidos por apenas um único médico, que tem um CRM ( documentação do conselho regional de medicina), um nome e sobrenome, e uma atuação. 
Esse médico tem a função de atender os pacientes. Além disso, ele também encaminha os pacientes para fazerem exames.

Todavia, antes dos pacientes passarem pelo médico, eles têm que ser atendidos primeiro pela atendente da UBS, que encaminha os pacientes e organiza as consultas. Essa atendente terá que conferir os dados dos pacientes ( contatos, CPF, cartão do SUS, número do prontuário, código da agência regional de saúde e o endereço). 
Depois disso, a atendente pode encaminhar os pacientes para o médico.


Modelo conceitual:


![modelo conceitual](https://user-images.githubusercontent.com/83674801/204658642-8396ed86-3b73-42aa-90eb-6fe9a5bc7e47.png)


Modelo Lógico:

![modelo logico](https://user-images.githubusercontent.com/83674801/204658685-ca4f963f-20b3-4328-959f-3b19affad3cf.png)

ps: Ao longo da implementação do sistema, algumas informações foram alteradas e não atualizadas nos modelos acima.  


Tecnologias usadas:

SGBD: PostgreSQL,
Linguagem de programação: Python,
Adaptador de Banco de dados (interoperabilidade do PostgreSQL e Python): psycopg2,
Biblioteca: tkinter (biblioteca para a interface gráfica do sistema).


Imagens gráfica do sistema:


![1](https://user-images.githubusercontent.com/83674801/204661076-e5ea4009-1e4e-4979-b9bd-c6294133f785.png)

![2](https://user-images.githubusercontent.com/83674801/204661095-2a968a3e-f640-410c-8938-eef7c621e43d.png)

![3](https://user-images.githubusercontent.com/83674801/204661113-5af631f0-c3ec-40fb-97f3-999b6e0df46e.png)

![4](https://user-images.githubusercontent.com/83674801/204661138-cb929431-feb1-4e21-83cf-3af92f9f9e3c.png)

![5](https://user-images.githubusercontent.com/83674801/204661172-d78c6264-1765-4828-9f3a-d6422b8024d9.png)

![7](https://user-images.githubusercontent.com/83674801/204661216-e82210ef-0db6-42d6-9636-94ca2250858f.png)

![84](https://user-images.githubusercontent.com/83674801/204661345-56171ac7-490f-43dc-b15a-44cd7b0d90bc.png)







