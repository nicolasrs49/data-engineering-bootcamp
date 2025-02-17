# Bootcamp Engenharia de Dados

Simulação de um projeto real de criação de pipelinas de integração de dados utilizando PostgreSQL (relacional), Airflow, DBT e Snowflake (analítico).

## Acesso bancos de dados

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
