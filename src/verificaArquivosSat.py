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

if os.path.exists(caminhoDaPastaSatXml):
    caminhos = [os.path.join(caminhoDaPastaSatXml, nome) for nome in os.listdir(caminhoDaPastaSatXml)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    xmlsSat = [arq for arq in arquivos if arq.lower().endswith('.xml')]
    print(xmlsSat)
else:
    os.mkdir('C:/Users/Adaão/Desktop/testeDeCriacao')
    if os.path.exists('C:/Users/Adaão/Desktop/testeDeCriacao'):
        print('O diretorio foi criado')
    else:
        print('O diretorio não pode ser criado')
'''
caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
jpgs = [arq for arq in arquivos if arq.lower().endswith(".jpg")]
'''
