import os.path
from datetime import datetime

pastaSat = 'C:/Program Files (x86)/Nox Automação/Fenix/SAT/XML'
pastaNfe = 'C:/Program Files (x86)/Nox Automação/Fenix/NFe/XML'
pastaDestino =

def verificaSeAPastaExiste(caminho):
    if os.path.exists(caminho):
        return True
    else:
        return False

if verificaSeAPastaExiste(pastaSat):
    caminhos = [os.path.join(pastaSat, nome) for nome in os.listdir(pastaSat)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq) and arq.lower().endswith('.xml')]
    print('printando arquivos')
    print(arquivos)



def verificaArquivos():
    now = datetime.now()
    mesPassado = 'foo'
    if now.month < 10:
        mesPassado = (str(now.year) + '0' + str(now.month - 1))
    else:
        mesEAno = (str(now.year) + str(now.month - 1))
    print(mesPassado)

verificaArquivos()