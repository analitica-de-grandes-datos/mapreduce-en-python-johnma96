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
    dict[linea[0]].append(int(linea[1]))
    
  else:
    dict[linea[0]] = [int(linea[1])]
lista = []
for i in dict.keys():
  suma = sum(dict[i])
  long = len(dict[i])
  prom = suma/long
  tupla = (i,float(suma),prom)
  lista.append(tupla)
lista.sort(key=lambda x: x[0])

for tupla in lista:
  
  line =  str(tupla[0]) + "\t" + str(tupla[1]) + "\t" + str(tupla[2]) + "\n"
  sys.stdout.write(line) 