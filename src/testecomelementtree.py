import os
import xmltodict
import dicttoxml
from xml.etree import ElementTree as elements

dadosx = xmltodict.parse(dados.content)
dadosxml = dicttoxml.dicttoxml(dadosx)

root = elements.fromstring(dadosxml)
levels = root.findall('.//IdentificacaoParlamentar')
for level in levels:
  name = level.find('NomeParlamentar').text
  code = level.find('CodigoParlamentar').text
  print(name)
  print(code)