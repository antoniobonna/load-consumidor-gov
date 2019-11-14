
### Normaliza nome das empresas
def parseName(name):
    ### Limpeza
    new_name = name.upper().replace(' (CONGLOMERADO)','')
    new_name = new_name.replace('-','').replace(',','')
    new_name = new_name.replace('S.A.','').replace('S A','').replace('S/A','').replace('S.A','')
    new_name = new_name.replace('LTDA.','')
    new_name = new_name.replace('CRÉDITO FINANCIAMENTO E INVESTIMENTO','').replace('CREDITO FINANCIAMENTO E INVESTIMENTO','').replace('CREDITO FINANCIAMENTO E INVESTIMENTOS','')
    new_name = new_name.replace('SOCIEDADE DE','')
    new_name = new_name.replace('FINANCIADORA','')
    new_name = new_name.strip()
    new_name = ' '.join(new_name.split())
    new_name = new_name.replace('CRÉDITO FINANCIAMENTO E INVESTIMENTO','').replace('CREDITO FINANCIAMENTO E INVESTIMENTO','').replace('CREDITO FINANCIAMENTO E INVESTIMENTOS','').strip()
    ### padronizacao
    
    if new_name.upper().startswith(('MERCADO LIBRE','MERCADOLI')):
        new_name = 'MERCADO LIVRE'
    elif new_name.upper().startswith('AMAZON'):
        new_name = 'AMAZON SHOPPING'
    elif new_name.upper().startswith('AMERICANAS'):
        new_name = 'AMERICANAS'
    elif new_name.upper().startswith('SUBMARINO'):
        new_name = 'SUBMARINO'
    elif new_name.upper().startswith('SHOPTIME'):
        new_name = 'SHOPTIME'
    elif new_name.upper().startswith(('MAGAZINE LUIZA','MAGAZINELUIZA')):
        new_name = 'MAGAZINE LUIZA'
    elif new_name.upper().startswith(('CASAS BAHIA','CASASBAHIA')):
        new_name = 'CASAS BAHIA'
    elif new_name.upper().startswith('PONTOFRIO'):
        new_name = 'PONTO FRIO'
    elif new_name.upper().startswith('EXTRA'):
        new_name = 'EXTRA'
    elif new_name.upper().startswith(('WALMEX','WALMART')):
        new_name = 'WALMART'
    elif new_name.upper().startswith('PICPAY'):
        new_name = 'PICPAY'
    elif new_name.upper().startswith(('MERCADO PAGO','MERCADOPAGO')):
        new_name = 'MERCADO PAGO'
    elif new_name.upper().startswith(('RECARGA CELULAR','RECARGAPAY')):
        new_name = 'RECARGAPAY'
    elif new_name.upper().startswith(('BANCO INTER','BANCOINTER')):
        new_name = 'INTER'
    elif new_name.upper().startswith('PAGSEGURO VENDAS'):
        new_name = 'PAGSEGURO VENDAS'
    elif new_name.upper().startswith('NEON'):
        new_name = 'NEON'
    elif new_name.upper().startswith(('BANCO NEXT','NEXT')):
        new_name = 'NEXT'
    elif new_name.upper().startswith('NUBANK'):
        new_name = 'NUBANK'
    elif new_name.upper().startswith(('BANCO ORIGINAL','ORIGINAL')):
        new_name = 'ORIGINAL'
    elif new_name.upper().startswith('STONE'):
        new_name = 'STONE'
    elif new_name.upper().startswith(('C6 BANK','C6BANK')):
        new_name = 'C6 BANK'
    elif new_name.upper().startswith('BS2 FLAMENGO'):
        new_name = 'BS2 FLAMENGO'
    elif new_name.upper().startswith(('BS2','BANCO BS2')):
        new_name = 'BS2'
    elif 'AGIBANK' in new_name.upper():
        new_name = 'AGIBANK'
    elif new_name.upper().startswith(('MEU PAG','MEUPAG')):
        new_name = 'MEU PAG!'
    elif new_name.upper().startswith('BANCO DIGIO'):
        new_name = 'DIGIO'
    elif new_name.upper().startswith(('PAN','BANCOPAN')):
        new_name = 'PAN'
    elif new_name.upper().startswith('CIELO'):
        new_name = 'CIELO'
    elif new_name.upper().startswith(('AME DIGITAL','AMEDIGITAL')):
        new_name = 'AME DIGITAL'
    elif new_name.upper().startswith('ITI'):
        new_name = 'ITI'
    elif new_name.upper().startswith('ITAUCARD'):
        new_name = 'ITAUCARD'
    elif new_name.upper().startswith('SANTANDER WAY'):
        new_name = 'SANTANDER WAY'
    elif new_name.upper().startswith('BRADESCO CART'):
        new_name = 'BRADESCO CARTOES'
    elif new_name.upper().startswith(('BANCO ITAÚ','ITAU')):
        new_name = 'ITAU'
    elif new_name.upper().startswith(('BRADESCO','BANCO.BRADESCO')):
        new_name = 'BRADESCO'
    elif new_name.upper().startswith('SANTANDER'):
        new_name = 'SANTANDER'
    elif new_name.upper().startswith(('BANCO DO BRASIL','BB')):
        new_name = 'BANCO DO BRASIL'
    elif new_name.upper().startswith('CAIXA'):
        new_name = 'CAIXA ECONOMICA FEDERAL'
    elif new_name.upper().startswith(('PAGBANK','PAGSEGURO')):
        new_name = 'PAGSEGURO'

    elif new_name == 'BB':
        new_name = 'BANCO DO BRASIL'    
    elif 'VIACREDI' in new_name:
        new_name = 'VIACREDI'
    elif 'SICOOB' in new_name:
        new_name = 'SICOOB'
    elif 'SICREDI' in new_name:
        new_name = 'SICREDI'
    elif 'UNIPRIME' in new_name:
        new_name = 'UNIPRIME' 
    elif 'UNICRED' in new_name:
        new_name = 'UNICRED'
    elif 'CRESOL' in new_name:
        new_name = 'CRESOL'
    elif 'ASCOOB' in new_name:
        new_name = 'ASCOOB'
    elif 'CREDJUST' in new_name:
        new_name = 'CREDJUST'
    elif new_name.startswith('NU '):
        new_name = 'NUBANK'
    elif new_name.startswith('COOPERATIVA') and new_name[-2] == '-':
        new_name = new_name[-1]
    else:
        new_name = new_name.replace('INTERMEDIUM', 'INTER').replace('BANCO INTER','INTER')
        new_name = new_name.replace('PAnew_nameRICANO', 'PAN').replace('BANCO PAN', 'PAN')
        new_name = new_name.replace('BONSUCESSO', 'BS2').replace('BANCO BS2', 'BS2').replace('GRUPO BS2 BS2','BS2')
        new_name = new_name.replace('BANCO NOSSA CAIXA', 'CAIXA ECONOMICA FEDERAL').replace('CAIXA ECONÔMICA FEDERAL', 'CAIXA ECONOMICA FEDERAL')
        new_name = new_name.replace('SANTANDER BANESPA', 'SANTANDER')
        new_name = new_name.replace('HSBC BANK BRASIL BANCO MULTIPLO', 'HSBC')
        new_name = new_name.replace('BANCO DAYCOVAL','DAYCOVAL')
        new_name = new_name.replace('BANCO BMG','BMG')
        new_name = new_name.replace('BANCO CITIBANK','CITIBANK')
        new_name = new_name.replace('BANCO ORIGINAL','ORIGINAL')
        new_name = new_name.replace('PAGSEGURO INTERNET','PAGSEGURO')
        new_name = new_name.replace('PAGSEGURO INTERNET','PAGSEGURO')
        new_name = new_name.replace('BANCO BMC','BMC')
        new_name = new_name.replace('ABCBRASIL','ABC-BRASIL')
        new_name = new_name.replace('BANCO BGN','BGN')
        new_name = new_name.replace('BANCO TOPÁZIO','BANCO TOPAZIO')
        new_name = new_name.replace('NOVO BANCO CONTINENTAL BANCO MÚLTIPLO','NOVO BANCO CONTINENTAL BANCO MULTIPLO')
        new_name = new_name.replace('AGIPLAN FINANCEIRA','AGIPLAN')
        new_name = new_name.replace('BANIF INTERNACIONAL DO FUNCHAL (BRASIL) EM LIQUIDAÇÃO ORDINÁRIA','BANIF')
        new_name = new_name.replace('BANCO DO ESTADO DO PARÁ','BANCO DO ESTADO DO PARA')
        new_name = new_name.replace('BANCO DE TOKYO MITSUBISHI UFJ BRASIL','BANCO DE TOKYOMITSUBISHI UFJ BRASIL')
        new_name = new_name.replace('BANCO A J RENNER','BANCO RENNER').replace('BANCO A.J. RENNER','BANCO RENNER')
        new_name = new_name.replace('BANCO BM&FBOVESPA DE SERVIÇOS DE LIQUIDAÇÃO E CUSTÓDIA','BANCO BM&FBOVESPA').replace('BANCO BM FBOVESPA DE SERVICOS DE LIQUIDACAO E CUSTODIA','BANCO BM&FBOVESPA')
        
    if new_name.endswith(' S'):
        new_name = new_name[:-2]
    return new_name
