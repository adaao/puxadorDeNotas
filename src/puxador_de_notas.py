"""
Autor: Adaão
Empresa: World Computer
data: 25/07/2019
"""

import os.path
import shutil
from datetime import datetime
from xml.dom import minidom


def defineDiretorioBox():
    if os.path.exists(os.path.expanduser('~/') + '/Box Sync'):
        return os.path.expanduser('~/') + '/Box Sync/contabilidade/'
    else:
        return os.path.expanduser('~/') + '/Box/contabilidade/'


def defineDiretorioNox():
    if os.path.exists('C:/Program Files (x86)/Nox Automação/Fenix'):
        return 'C:/Program Files (x86)/Nox Automação/Fenix'
    else:
        if os.path.exists('C:/Program Files (x86)/Nox Automação/Fenix Combo'):
            return 'C:/Program Files (x86)/Nox Automação/Fenix Combo'


def formataMes(mes):
    if mes < 10:
        mesFormatado = '0' + str(mes)
    else:
        mesFormatado = str(mes)
    return mesFormatado


def calculaMesPassado(now):
    if (now.month == 1):
        mesPassado = 12
    else:
        mesPassado = now.month - 1
    return mesPassado


def calculaAno(now):
    if (now.month == 1):
        ano = now.year - 1
    else:
        ano = now.year
    return ano


def filtraArquivosXml(diretorio):
    if os.path.exists(diretorio):
        arquivos = [os.path.join(diretorio, arquivo) for arquivo in os.listdir(diretorio)]
        arquivosXml = [arq for arq in arquivos if os.path.isfile(arq) and arq.lower().endswith('.xml')]
        return arquivosXml
    else:
        print('Os diretorios ou os arquivos xml não foram encontrados...')
        input('Pressione enter para sair')
        exit()


def criaDiretorio(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)


def geraArquivoZipado(diretorioDestino, diretorioOrigem):
    shutil.make_archive(diretorioDestino, 'zip', diretorioOrigem)


def separaArquivosSatPorDataDeEmissao(ano, mes, diretorioSat, diretorioBox):
    arquivos = filtraArquivosXml(diretorioSat)
    tagSat = 'dEmi'
    if len(arquivos) > 0:
        nomeDoMes = retornaNomeDoMes(mes)
        diretorioDeDestinoSat = diretorioSat + '/' + nomeDoMes
        diretorioBoxDeDestinoSat = diretorioBox + str(ano) + '/' + nomeDoMes + '/' + nomeDoMes + ' - SAT/'
        criaDiretorio(diretorioDeDestinoSat)
        mesFormatado = formataMes(mes)
        criaDiretorio(diretorioBox + str(ano) + '/' + nomeDoMes)
        print('==================== arquivos sat ====================')
        for arquivo in arquivos:
            if (arquivo[51:53] == 'AD') or (arquivo[57:59] == 'AD'):
                xmldoc = minidom.parse(arquivo)
                dataDeEmissao = xmldoc.getElementsByTagName(tagSat)[0]
                if str(dataDeEmissao.firstChild.data)[0:4].__eq__(str(ano)) and (str(dataDeEmissao.firstChild.data)[4:6].__eq__(mesFormatado)):
                    print(arquivo)
                    print('data de emissao: ' + str(dataDeEmissao.firstChild.data))
                    shutil.copy(arquivo, diretorioDeDestinoSat)
        if len(filtraArquivosXml(diretorioDeDestinoSat)) > 0:
            geraArquivoZipado(diretorioBoxDeDestinoSat, diretorioDeDestinoSat)


def separaArquivosNfePorDataDeEmissao(ano, mes, diretorioNfe, diretorioBox):
    arquivos = filtraArquivosXml(diretorioNfe)
    if len(arquivos) > 0:
        nomeDoMes = retornaNomeDoMes(mes)
        diretorioDeDestinoNfe = diretorioNfe + '/' + nomeDoMes
        diretorioDeDestinoBox = diretorioBox + str(ano) + '/' + nomeDoMes + '/' + nomeDoMes + ' - NFE'
        criaDiretorio(diretorioDeDestinoNfe)
        mesFormatado = formataMes(mes)
        criaDiretorio(diretorioBox + str(ano) + '/' + nomeDoMes)
        print('==================== arquivos nfe ====================')
        for arquivo in arquivos:
            if (arquivo[::-1][0:7] == 'lmx.efn'):
                xmldoc = minidom.parse(arquivo)
                dataDeEmissao = xmldoc.getElementsByTagName('dhEmi')[0]
                if str(dataDeEmissao.firstChild.data)[0:4].__eq__(str(ano)) and (str(dataDeEmissao.firstChild.data)[5:7].__eq__(mesFormatado)):
                    print(arquivo)
                    print('data de emissao: ' + str(dataDeEmissao.firstChild.data))
                    shutil.copy(arquivo, diretorioDeDestinoNfe)
            if (arquivo[::-1][0:7] == 'lmx.ecc') or (arquivo[::-1][0:7] == 'lmx.eve'):
                xmldoc = minidom.parse(arquivo)
                dataDeEmissao = xmldoc.getElementsByTagName('dhEvento')[0]
                if str(dataDeEmissao.firstChild.data)[0:4].__eq__(str(ano)) and (str(dataDeEmissao.firstChild.data)[5:7].__eq__(mesFormatado)):
                    print(arquivo)
                    print('data de emissao: ' + str(dataDeEmissao.firstChild.data))
                    shutil.copy(arquivo, diretorioDeDestinoNfe)
            if (arquivo[::-1][0:7] == 'lmx.uni'):
                xmldoc = minidom.parse(arquivo)
                if len(xmldoc.getElementsByTagName('dhRcbto')) == 1:
                    dataDeEmissao = xmldoc.getElementsByTagName('dhRcbto')[0]
                    if str(dataDeEmissao.firstChild.data)[0:4].__eq__(str(ano)) and (str(dataDeEmissao.firstChild.data)[5:7].__eq__(mesFormatado)):
                        print(arquivo)
                        print('data de emissao: ' + str(dataDeEmissao.firstChild.data))
                        shutil.copy(arquivo, diretorioDeDestinoNfe)
        if len(filtraArquivosXml(diretorioDeDestinoNfe)) > 0:
            geraArquivoZipado(diretorioDeDestinoBox, diretorioDeDestinoNfe)


def retornaNomeDoMes(mes):
    switcher = {
        1: '01 - JANEIRO',
        2: '02 - FEVEREIRO',
        3: '03 - MARÇO',
        4: '04 - ABRIL',
        5: '05 - MAIO',
        6: '06 - JUNHO',
        7: '07 - JULHO',
        8: '08 - AGOSTO',
        9: '09 - SETEMBRO',
        10: '10 - OUTUBRO',
        11: '11 - NOVEMBRO',
        12: '12 - DEZEMBRO'
    }
    return switcher.get(mes, 'mes invalido')


def main():
    print('Salvando arquivos fiscais...')
    diretorioNox = str(defineDiretorioNox())
    diretorioSat = diretorioNox + '/SAT/XML'
    diretorioNfe = diretorioNox + '/NFe/XML'
    diretorioBox = defineDiretorioBox()
    now = datetime.now()
    separaArquivosNfePorDataDeEmissao(calculaAno(now), calculaMesPassado(now), diretorioNfe, diretorioBox)
    separaArquivosSatPorDataDeEmissao(calculaAno(now), calculaMesPassado(now), diretorioSat, diretorioBox)


main()
