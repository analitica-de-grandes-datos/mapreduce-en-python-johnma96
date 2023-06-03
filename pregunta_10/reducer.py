#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

dict =  {}
for row in sys.stdin:
  linea = row.strip()
  linea = linea.split(";")
  clave = int(linea[0])
  valor = linea[1]
  valor = valor.split(",")
  for v in valor:
    if v in dict.keys():
      dict[v].append(clave)
    else:
      dict[v] = [clave]
lista = []
for i in dict.keys():
  valores = dict[i]
  val = valores.sort()
  tupla = (i,valores)
  lista.append(tupla)

lista.sort(key=lambda x: x[0])

for tupla in lista:
  letra =  tupla[0]
  valores = []
  for i in tupla[1]:
    valores.append(str(i))
  valores = ",".join(valores)
  line =  letra + "\t" + valores + "\n"
  #line = valores
  sys.stdout.write(line) 