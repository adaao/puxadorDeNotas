import os
from xml.etree import ElementTree

file_name = 'AD35190521365621000149590005545290002821120664.xml'
full_file = os.path.abspath(os.path.join('data', file_name))

dom = ElementTree.parse(full_file)
print(dom)
