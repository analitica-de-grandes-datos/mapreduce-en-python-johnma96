#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from datetime import date
dict =  {}

for row in sys.stdin:
  linea = row.strip()
  linea = linea.split(";")
  if linea[0] in dict.keys():
    dict[linea[0]] +=  1
    
  else:
    dict[linea[0]] = 1


lista = [(i,dict[i]) for i in dict.keys()]
lista.sort(key=lambda x: x[0])

for tupla in lista:
  
  line =  str(tupla[0]) + "\t" + str(tupla[1]) + "\n"
  sys.stdout.write(line) 