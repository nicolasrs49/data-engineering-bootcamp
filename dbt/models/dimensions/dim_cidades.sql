{{ config(materialized='table') }}

SELECT
    id_cidades AS cidade_id,
    nome_cidade,
    id_estados as estado_id,
    data_inclusao,
    data_atualizacao
FROM {{ ref("stg_cidades") }}