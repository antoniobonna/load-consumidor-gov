#!/bin/bash

### Definicao de variaveis
LOG="/var/log/scripts/scripts.log"
DIR="/home/ubuntu/scripts/load-dados-consumidor-gov"
DUMP="/home/ubuntu/dump"
STARTDATE=$(date +'%F %T')
SCRIPTNAME="load-dados-consumidor-gov.sh"
BOT="bot_message.py"

horario()
{
	date +%d/%m/%Y" - "%H:%M:%S
}
export -f horario

stagingDados()
{
	FILE=$1
	time python ${DIR}/${FILE}
	echo -e "$(horario): Script $FILE executado.\n-\n"
}
export -f stagingDados

LoadDW()
{
	FILE=$1
	time psql -d torkcapital -f ${DIR}/${FILE}
	echo -e "$(horario): Script $FILE executado.\n-\n"
}
export -f LoadDW

LoadHist()
{
	time (psql -d torkcapital -c "COPY (table dados_consumidor_gov.dados_abertos_stg) TO '/home/ubuntu/dump/dados_abertos.txt';"
	psql -d torkcapital -c "COPY dados_consumidor_gov.dados_abertos_hist FROM '/home/ubuntu/dump/dados_abertos.txt';"
	psql -d torkcapital -c "VACUUM ANALYZE dados_consumidor_gov.dados_abertos_hist;"
	psql -d torkcapital -c "TRUNCATE dados_consumidor_gov.dados_abertos_stg;")
	echo -e "$(horario): Tabela dados_abertos transferida para dados historicos.\n-\n"
}
export -f LoadHist

python ${DIR}/${BOT} START DAILY

### Carrega arquivos nas tabelas staging

echo -e "$(horario): Inicio do staging.\n-\n"

ListaArquivos="load_dados.py"
for FILE in $ListaArquivos; do
	stagingDados $FILE
done

### Carrega dados no DW

echo -e "$(horario): Inicio da carga no DW.\n-\n"

ListaArquivos="etl_dados_consumidor.sql"
for FILE in $ListaArquivos; do
	LoadDW $FILE
done

### Limpa tabelas staging e carrega no historico

echo -e "$(horario): Inicio da limpeza do staging.\n-\n"

LoadHist $TABLE

### Remove arquivos temporarios e escreve no log

rm -f ${DUMP}/*.txt

ENDDATE=$(date +'%F %T')
echo "$SCRIPTNAME;$STARTDATE;$ENDDATE" >> $LOG

echo -e "$(horario):Fim da execucao.\n"

python ${DIR}/${BOT} "END"

exit 0
