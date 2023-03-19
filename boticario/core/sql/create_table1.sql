DROP TABLE IF EXISTS official.tabela1;
CREATE TABLE official.tabela1 AS
SELECT TRUNC(
               date_trunc(
                       'month',
                       CASE
                           WHEN filename = 'Base 2017 (1).xlsx' THEN DATEADD(YEAR, -2, data_venda)
                           WHEN filename = 'Base_2018 (1).xlsx' THEN DATEADD(YEAR, 1, data_venda)
                           ELSE data_venda
                           END)) AS ano_mes,
       SUM(qtd_venda)            AS qtd_venda
FROM load.base
GROUP BY ano_mes
ORDER BY ano_mes;