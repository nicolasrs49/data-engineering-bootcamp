# Bootcamp Engenharia de Dados

Simulação de um projeto real de criação de pipelinas de integração de dados utilizando PostgreSQL (relacional), Airflow, DBT e Snowflake (analítico).

## Acesso bancos de dados* 

\* Aparentemente as credenciais do curso mudaram, pois não está mais acessível.

Banco de dados relacional de um sistema de vendas da concessionária:

- host: 159.223.187.110
- dbname ou database ou banco de dados: novadrive
- user ou usuário: etlreadonly
- password ou senha: novadrive376A@
- port ou porta: 5432

## Acessar Sistema de Vendas

Para acesso ao Sistema de Vendas:

http://143.244.215.137:3002/

Login: vendedor1

Senha: ia_nova_drive

Para consultar uma venda pelo ID da venda:

http://143.244.215.137:3002/procura

## Instalação e Setup do Airflow

Utilizar os scripts no arquivo "airflow-install.txt".
A instalação será realizada em uma máquina EC2 da AWS utilizando o SO Ubuntu.

## Setup Snowflake

Sobre credenciais, utilizar o arquivo "snowflake-credentials.txt".
Para criação do database, schema e tables, utilizar os scripts no arquivo "snowflake-setup.sql".

## DBT

Utilizando DBT Cloud para criar um pipeline de transformação, com controle de versionamento e integrado com Github, para estar preparado para um futuro CI/CD.

## Dashboard

Enquanto o profissional responsável pela construção de dashboards e outras análises não é contratado na NovaDrive, foi criado um dashboard simples utilizando o Looker Studio para acompanhar a performance de vendas das concessionárias.

[Acesso ao Dashboard aqui.](https://lookerstudio.google.com/reporting/48df0d6a-a046-46ae-a540-06788324b373)