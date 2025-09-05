SELECT
  r.SAIDAS_ID AS "Código Saída",
  r.SAIDA_DATA_SAIDA AS "Data da Saída",
  r.OPERACAO_NOME AS "Operação",
  r.CLIENTES_ID AS "Código Cliente",
  r.CLIENTE_NOME1 AS "Nome Cliente",
  r.ROTA_NOME AS "Rota",
  r.DISTRITO_NOME AS "Distrito",
  s.SAIDA_PLACA_VEICULO AS "Placa Veículo",
  r.PRODUTOS_ID AS "Código Produto",
  r.PRODUTO_NOME AS "Produto",
  r.SAIDAITEM_QUANTIDADE AS "Quantidade",
  r.SAIDAITEM_TOTAL_LIQUIDO AS "Valor Total"
FROM RSAIDAS003 r
JOIN SAIDAS s ON s.SAIDAS_ID = r.SAIDAS_ID
