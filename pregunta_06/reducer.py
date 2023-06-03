#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

dict =  {}
for row in sys.stdin:
  linea = row.strip()
  linea = linea.split(";")
  if linea[0] in dict.keys():
    if float(linea[1]) > dict[linea[0]][1]:
      dict[linea[0]][1] = float(linea[1])
    if float(linea[1]) < dict[linea[0]][0]:
      dict[linea[0]][0] = float(linea[1])
    else:
      continue
  else:
    dict[linea[0]] = [float(linea[1]),float(linea[1])]
lista = [(i,dict[i][0],dict[i][1]) for i in dict.keys()]
lista.sort(key=lambda x: x[0])

for tupla in lista:
  line =  tupla[0] + "\t" + str(tupla[2]) + "\t" + str(tupla[1]) + "\n"
  sys.stdout.write(line) 