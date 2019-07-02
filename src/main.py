import os.path
from datetime import datetime
from xml.dom import minidom
print('Salvando arquivos fiscais...')
diretorioSat = 'C:/Program Files (x86)/Nox Automação/Fenix/SAT/XML'
pastaNfe = 'C:/Program Files (x86)/Nox Automação/Fenix/NFe/XML'
pastaDestinoSat = 'C:/Users/adaao/Desktop'
tag = 'bar'

now = datetime.now()

if now.month < 10:
    nowInStr = str(now.year) + '0' + str(now.month) + str(now.day)
else:
    nowInStr = str(now.year) + str(now.month) + str(now.day)

def calculaMesPassado():
    if (now.month - 1) < 10:
        mesPassado = (str(now.year) + '0' + str(now.month - 1))
    else:
        mesPassado = (str(now.year) + str(now.month - 1))
    return mesPassado
    

def verificaArquivos(diretorio):
    
    if os.path.exists(diretorio):
        arquivos = [os.path.join(diretorio, arquivo) for arquivo in os.listdir(diretorio)]
        arquivosXml = [arq for arq in arquivos if os.path.isfile(arq) and arq.lower().endswith('.xml')]
        separaArquivosPorDataDeEmissao(arquivosXml, calculaMesPassado())
    else:
        print('Os diretorios que deveriam conter os arquivos não foram encontrados...')
        input()

def separaArquivosPorDataDeEmissao(arquivos, mesPassado):
    for arquivo in arquivos:
        xmldoc = minidom.parse(arquivo)
        dataDeEmissao = xmldoc.getElementsByTagName('dEmi')[0]
        print(arquivo)
        print('data de emissao: ' + str(dataDeEmissao.firstChild.data))
        print('{} == {} = {}'.format(str(dataDeEmissao.firstChild.data), nowInStr, str(dataDeEmissao.firstChild.data) == nowInStr))
        print(str(dataDeEmissao.firstChild.data)[4:6].__eq__(mesPassado))

    print(retornaNomeDoMes(now.month))

def criaDiretorioDeDestino(tipoDeArquivo, mes, ano):

    if not (os.path.exists('C:/arquivos fiscais/' + ano + '/' + mes + '/' + tipoDeArquivo)):
        os.makedirs('C:/arquivos fiscais/' + ano + '/' + mes + '/' + tipoDeArquivo)

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
    print(switcher.get(mes, "Mês inválido"))

criaDiretorioDeDestino('NFE', '00 - TESTE', '2019')
'''
verificaArquivos(diretorioSat)
'''
'''input('Arquivos salvos, digite enter para sair.')'''
