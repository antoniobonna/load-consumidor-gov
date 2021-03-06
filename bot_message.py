import telepot
import emoji
from datetime import datetime, timedelta
from sys import argv

### Carrega emojis
OK = emoji.emojize(':heavy_check_mark:', use_aliases=True)
NOK = emoji.emojize(':cross_mark:', use_aliases=True)

### Ids do Telegram

botID = '784006906:AAF1qZj6fA9HdfdTijq04rmJ8nb5O43bmUg'
channelID = '@datasciencetork'

### variaveis
logfile = '/var/log/scripts/crawler-play-store.log'

if argv[1] == 'START':
    message = 'Crawler do Google Play iniciado ' + OK
else:
    with open (logfile, 'r') as ifile:
        if 'ERROR' in ifile.read():
            message= 'Crawler do Google Play finalizado com erros ' + NOK + '\n\nFavor verificar o log de execução'
        else:
            message = 'Crawler do Google Play finalizado com sucesso ' + OK

bot = telepot.Bot(botID)
bot.sendMessage(channelID,message)

