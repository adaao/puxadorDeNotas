import os.path
from datetime import datetime
from xml.dom import minidom

print('Salvando arquivos fiscais...')
diretorioSat = 'C:/Program Files (x86)/Nox Automação/Fenix/SAT/XML'
diretorioNfe = 'C:/Program Files (x86)/Nox Automação/Fenix/NFe/XML'
tagSat = 'dEmi'
tagNfe = 'dhEmi'


now = datetime.now()


if now.month < 10:
    nowInStr = str(now.year) + '0' + str(now.month) + str(now.day)
else:
    nowInStr = str(now.year) + str(now.month) + str(now.day)


def formataMes(mes):
    if mes < 10:
        mesFormatado = '0' + str(mes)
    else:
        mesFormatado = str(mes)
    return mesFormatado


def calculaMesPassado():
    if (now.month == 1):
        mesPassado = 12
    else:
        mesPassado = now.month - 1
    return mesPassado


def calculaAno():
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
        input()


def separaArquivosSatPorDataDeEmissao(mesPassadoFormatado):
    arquivos = filtraArquivosXml(diretorioSat)
    for arquivo in arquivos:
        if (arquivo[51:53] == 'AD'):
            xmldoc = minidom.parse(arquivo)
            dataDeEmissao = xmldoc.getElementsByTagName(tagSat)[0]

            '''
            print(arquivo)
            
            print('{} == {} = {}'.format(str(dataDeEmissao.firstChild.data), nowInStr, str(dataDeEmissao.firstChild.data) == nowInStr))
            nomeDoMes = retornaNomeDoMes(calculaMesPassado())
            print('mes passado: ' + nomeDoMes)
            '''
            if (str(dataDeEmissao.firstChild.data)[4:6].__eq__(mesPassadoFormatado)):
                print('data de emissao: ' + str(dataDeEmissao.firstChild.data))
                print('narf')
            else:
                print('troz')


def separaArquivosNfePorDataDeEmissao(mesPassadoFormatado):
    print('================= arquivos nfe ========================')
    arquivos = filtraArquivosXml(diretorioNfe)
    for arquivo in arquivos:
        if (arquivo[::-1][0:7] == 'lmx.efn'):
            xmldoc = minidom.parse(arquivo)
            dataDeEmissao = xmldoc.getElementsByTagName(tagNfe)[0]

            '''
            print(arquivo)
            print('data de emissao: ' + str(dataDeEmissao.firstChild.data))
            print('{} == {} = {}'.format(str(dataDeEmissao.firstChild.data), nowInStr, str(dataDeEmissao.firstChild.data) == nowInStr))
            nomeDoMes = retornaNomeDoMes(calculaMesPassado())
            print('mes passado: ' + nomeDoMes)
            '''
            if (str(dataDeEmissao.firstChild.data)[5:7].__eq__(mesPassadoFormatado)):
                print('narf')
            else:
                print(str(dataDeEmissao.firstChild.data))

def criaDiretoriosDeDestino(ano, mes):
    diretorioSat = 'C:/arquivos fiscais/' + ano + '/' + mes + '/SAT'
    diretorioNfe = 'C:/arquivos fiscais/' + ano + '/' + mes + '/NFE'

    if not (os.path.exists(diretorioSat)):
        os.makedirs(diretorioSat)

    if not (os.path.exists(diretorioNfe)):
        os.makedirs(diretorioNfe)


def retornaNomeDoMes(mes):
    switcher = {
        1: "01 - JANEIRO",
        2: "02 - FEVEREIRO",
        3: "03 - MARÇO",
        4: "04 - ABRIL",
        5: "05 - MAIO",
        6: "06 - JUNHO",
        7: "07 - JULHO",
        8: "08 - AGOSTO",
        9: "09 - SETEMBRO",
        10: "10 - OUTUBRO",
        11: "11 - NOVEMBRO",
        12: "12 - DEZEMBRO"
    }
    return switcher.get(mes, 'mes invalido')


separaArquivosNfePorDataDeEmissao(formataMes(calculaMesPassado()))
criaDiretoriosDeDestino(str(calculaAno()), retornaNomeDoMes(calculaMesPassado()))
separaArquivosSatPorDataDeEmissao(formataMes(calculaMesPassado()))

