DROP TABLE IF EXISTS official.tabela2;
CREATE TABLE official.tabela2 AS
SELECT marca, linha, SUM(qtd_venda) AS qtd_venda
FROM load.base
GROUP BY marca, linha;