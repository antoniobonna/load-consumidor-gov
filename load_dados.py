# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:18:31 2019

@author: abonna
"""

import os
import csv
import credentials
import psycopg2
from subprocess import call
from companies import parseName

### Definicao das variaveis
indir = '/home/ubuntu/dump/dados_consumidor_gov/'
outdir = '/home/ubuntu/scripts/load-dados-consumidor-gov/parsed/'
new_file = 'dados.csv'
files = [f for f in os.listdir(indir) if f.endswith('.csv')]
tablename = 'dados_consumidor_gov.dados_abertos_stg'

DATABASE, HOST, USER, PASSWORD = credentials.setDatabaseLogin()

### funcao que cria data no formato banco de dados
def parse_date(date):
    newdate = date[6:] + '-' + date[3:5] + '-' + date[:2]
    return newdate

### Iteracao sobre os diretorios e parser dos CSVs
with open(outdir+new_file,'w', newline="\n", encoding="utf-8") as ofile: ### arquivo temporario
    writer = csv.writer(ofile, delimiter=';')
    for file in files:
        with open(indir+file, 'r', encoding='utf-8') as ifile:
            reader = csv.reader(ifile, delimiter=';')
            for row in reader:
                if row[8] in ['Varejo','Bancos, Financeiras e Administradoras de Cartão','Comércio Eletrônico','Empresas de Intermediação de Serviços / Negócios','Empresas de Pagamento Eletrônico']:
                    row[5] = parse_date(row[5])
                    row[7] = parseName(row[7])
                    writer.writerow(row)

        os.remove(outdir+file)

### conecta no banco de dados
db_conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(DATABASE, USER, HOST, PASSWORD))
cursor = db_conn.cursor()
print('Connected to the database')
### copy
with open(outdir+new_file, 'r') as ifile:
    SQL_STATEMENT = "COPY %s FROM STDIN WITH CSV DELIMITER AS ';' NULL AS ''"
    print("Executing Copy in "+tablename)
    cursor.copy_expert(sql=SQL_STATEMENT % tablename, file=ifile)
    db_conn.commit()
cursor.close()
db_conn.close()

### VACUUM ANALYZE
call('psql -d torkcapital -c "VACUUM VERBOSE ANALYZE '+tablename+'";',shell=True)
