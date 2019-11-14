
-- dados_consumidor_gov_dw.data

\! echo "Carregando dados na tabela data..."

INSERT INTO dados_consumidor_gov_dw.data
SELECT distinct data, date_part('week', data),date_part('month', data),date_part('year', data)
	FROM dados_consumidor_gov.dados_abertos_stg WHERE data not in (SELECT data FROM dados_consumidor_gov_dw.data)
ORDER BY 1;

VACUUM ANALYZE dados_consumidor_gov_dw.data;

----------------------------------------------------------------------------

-- dados_consumidor_gov_dw.assunto

\! echo "Carregando dados na tabela assunto..."

INSERT INTO dados_consumidor_gov_dw.assunto(assunto)
SELECT distinct assunto
FROM dados_consumidor_gov.dados_abertos_stg
EXCEPT
SELECT assunto FROM dados_consumidor_gov_dw.assunto
ORDER BY 1;

VACUUM ANALYZE dados_consumidor_gov_dw.assunto;

----------------------------------------------------------------------------

-- dados_consumidor_gov_dw.cidade

\! echo "Carregando dados na tabela cidade..."

INSERT INTO dados_consumidor_gov_dw.cidade(cidade,uf,regiao)
SELECT distinct cidade,uf,regiao
FROM dados_consumidor_gov.dados_abertos_stg
EXCEPT
SELECT cidade,uf,regiao FROM dados_consumidor_gov_dw.cidade
ORDER BY 1;

VACUUM ANALYZE dados_consumidor_gov_dw.cidade;

----------------------------------------------------------------------------

-- dados_consumidor_gov_dw.como_comprou_contratou

\! echo "Carregando dados na tabela como_comprou_contratou..."

INSERT INTO dados_consumidor_gov_dw.como_comprou_contratou(como_comprou_contratou)
SELECT distinct como_comprou_contratou
FROM dados_consumidor_gov.dados_abertos_stg
EXCEPT
SELECT como_comprou_contratou FROM dados_consumidor_gov_dw.como_comprou_contratou
ORDER BY 1;

VACUUM ANALYZE table dados_consumidor_gov_dw.como_comprou_contratou;

----------------------------------------------------------------------------

-- dados_consumidor_gov_dw.empresa

\! echo "Carregando dados na tabela empresa..."

INSERT INTO dados_consumidor_gov_dw.empresa(empresa)
SELECT distinct nome_fantasia
FROM dados_consumidor_gov.dados_abertos_stg
EXCEPT
SELECT empresa FROM dados_consumidor_gov_dw.empresa
ORDER BY 1;

VACUUM ANALYZE dados_consumidor_gov_dw.empresa;

----------------------------------------------------------------------------

-- dados_consumidor_gov_dw.faixa_etaria

-- \! echo "Carregando dados na tabela faixa_etaria..."

-- INSERT INTO dados_consumidor_gov_dw.faixa_etaria(faixa_etaria)
-- SELECT distinct faixa_etaria
-- FROM dados_consumidor_gov.dados_abertos_stg
-- ORDER BY 1;

-- VACUUM ANALYZE dados_consumidor_gov_dw.faixa_etaria;

----------------------------------------------------------------------------

-- dados_consumidor_gov_dw.problema

\! echo "Carregando dados na tabela problema..."

INSERT INTO dados_consumidor_gov_dw.problema(problema,grupo_problema)
SELECT distinct problema,grupo_problema
FROM dados_consumidor_gov.dados_abertos_stg
EXCEPT
SELECT problema,grupo_problema FROM dados_consumidor_gov_dw.problema
ORDER BY 1;

VACUUM ANALYZE dados_consumidor_gov_dw.problema;

----------------------------------------------------------------------------

-- dados_consumidor_gov_dw.procurou_empresa

-- \! echo "Carregando dados na tabela procurou_empresa..."

-- INSERT INTO dados_consumidor_gov_dw.procurou_empresa(procurou_empresa)
-- SELECT distinct CASE WHEN procurou_empresa = 'N' THEN False ELSE True END
-- FROM dados_consumidor_gov.dados_abertos_stg
-- ORDER BY 1;

-- VACUUM ANALYZE dados_consumidor_gov_dw.procurou_empresa;

----------------------------------------------------------------------------

-- dados_consumidor_gov_dw.respondida

-- \! echo "Carregando dados na tabela respondida..."

-- INSERT INTO dados_consumidor_gov_dw.respondida(respondida)
-- SELECT distinct CASE WHEN respondida = 'N' THEN False ELSE True END
-- FROM dados_consumidor_gov.dados_abertos_stg
-- ORDER BY 1;

-- VACUUM ANALYZE dados_consumidor_gov_dw.respondida;

----------------------------------------------------------------------------

-- dados_consumidor_gov_dw.segmento_de_mercado

\! echo "Carregando dados na tabela segmento_de_mercado..."

INSERT INTO dados_consumidor_gov_dw.segmento_de_mercado(segmento_de_mercado)
SELECT distinct segmento_de_mercado
FROM dados_consumidor_gov.dados_abertos_stg
EXCEPT
SELECT segmento_de_mercado FROM dados_consumidor_gov_dw.segmento_de_mercado
ORDER BY 1;

VACUUM ANALYZE dados_consumidor_gov_dw.segmento_de_mercado;

----------------------------------------------------------------------------

-- dados_consumidor_gov_dw.sexo

-- \! echo "Carregando dados na tabela sexo..."

-- INSERT INTO dados_consumidor_gov_dw.sexo(sexo)
-- SELECT distinct sexo
-- FROM dados_consumidor_gov.dados_abertos_stg
-- ORDER BY 1;

-- VACUUM ANALYZE dados_consumidor_gov_dw.sexo;

----------------------------------------------------------------------------

-- dados_consumidor_gov_dw.situacao
\! echo "Carregando dados na tabela situacao..."

INSERT INTO dados_consumidor_gov_dw.situacao(situacao)
SELECT distinct situacao
FROM dados_consumidor_gov.dados_abertos_stg
EXCEPT
SELECT situacao FROM dados_consumidor_gov_dw.situacao
ORDER BY 1;

VACUUM ANALYZE dados_consumidor_gov_dw.situacao;

----------------------------------------------------------------------------

-- dados_consumidor_gov_dw.dados_consumidor

\! echo "Carregando dados na tabela fato dados_consumidor..."

COPY(
SELECT d.data, e.empresa_id, c.cidade_id, s.sexo_id, fa.faixa_etaria_id, se.segmento_de_mercado_id, a.assunto_id, p.problema_id, co.como_comprou_contratou_id, pr.procurou_empresa_id, si.situacao_id, 
	r.respondida_id, AVG(f.tempo_resposta)::int, AVG(f.nota_do_consumidor)::real, SUM(f.total)	
	FROM dados_consumidor_gov.dados_abertos_stg f
	JOIN dados_consumidor_gov_dw.data d ON d.data=f.data
	JOIN dados_consumidor_gov_dw.empresa e ON e.empresa=f.nome_fantasia
	JOIN dados_consumidor_gov_dw.cidade c ON c.cidade=f.cidade AND c.uf=f.uf
	JOIN dados_consumidor_gov_dw.sexo s ON s.sexo=f.sexo
	JOIN dados_consumidor_gov_dw.faixa_etaria fa ON fa.faixa_etaria=f.faixa_etaria
	JOIN dados_consumidor_gov_dw.segmento_de_mercado se ON se.segmento_de_mercado=f.segmento_de_mercado
	JOIN dados_consumidor_gov_dw.assunto a ON a.assunto=f.assunto
	JOIN dados_consumidor_gov_dw.problema p ON p.problema=f.problema AND f.grupo_problema = p.grupo_problema
	JOIN dados_consumidor_gov_dw.como_comprou_contratou co ON co.como_comprou_contratou=f.como_comprou_contratou
	JOIN dados_consumidor_gov_dw.procurou_empresa pr ON CASE WHEN f.procurou_empresa = 'N' THEN False ELSE True END = pr.procurou_empresa
	JOIN dados_consumidor_gov_dw.situacao si ON si.situacao=f.situacao
	JOIN dados_consumidor_gov_dw.respondida r ON CASE WHEN f.respondida = 'N' THEN False ELSE True END = r.respondida
	GROUP BY d.data, e.empresa_id, c.cidade_id, s.sexo_id, fa.faixa_etaria_id, se.segmento_de_mercado_id, a.assunto_id, p.problema_id, co.como_comprou_contratou_id, pr.procurou_empresa_id, si.situacao_id, 
	r.respondida_id
) to '/home/ubuntu/dump/dados_consumidor.txt';
COPY dados_consumidor_gov_dw.dados_consumidor FROM '/home/ubuntu/dump/dados_consumidor.txt';

VACUUM ANALYZE dados_consumidor_gov_dw.dados_consumidor;
