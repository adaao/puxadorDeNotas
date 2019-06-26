import os.path
from datetime import datetime
now = datetime.now()
print (now.month - 1)
print (now.year)
if now.month < 10:
    mesEAno = (str(now.year) + '0' + str(now.month))
else:
    mesEAno = (str(now.year) + str(now.month))
print(mesEAno)

caminhoDaPastaSatXml = 'C:/Program Files (x86)/Nox Automação/Fenix/SAT/XML'
caminhoDaPastaNfeXml = 'C:/Program Files (x86)/Nox Automação/Fenix/NFe/XML'


'''
caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
jpgs = [arq for arq in arquivos if arq.lower().endswith(".jpg")]
'''