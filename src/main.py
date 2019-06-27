import os.path
from datetime import datetime
'''from bs4 import BeautifulSoup'''
from xml.dom import minidom

pastaSat = 'C:/Program Files (x86)/Nox Automação/Fenix/SAT/XML'
pastaNfe = 'C:/Program Files (x86)/Nox Automação/Fenix/NFe/XML'
pastaDestino = 'foo'

def verificaSeAPastaExiste(caminho):
    if os.path.exists(caminho):
        return True
    else:
        return False


def verificaArquivos():
    now = datetime.now()
    mesPassado = 'foo'
    if now.month < 10:
        mesPassado = (str(now.year) + '0' + str(now.month - 1))
    else:
        mesPassado = (str(now.year) + str(now.month - 1))

    if verificaSeAPastaExiste(pastaSat):
        caminhos = [os.path.join(pastaSat, nome) for nome in os.listdir(pastaSat)]
        arquivos = [arq for arq in caminhos if os.path.isfile(arq) and arq.lower().endswith('.xml')]

    for arquivo in arquivos:
        xmldoc = minidom.parse(arquivo)
        dataDeEmissao = xmldoc.getElementsByTagName('dEmi')
        print(arquivo)
        print('data de emissao: ')
        for x in dataDeEmissao:
            print(x.toxml())

verificaArquivos()