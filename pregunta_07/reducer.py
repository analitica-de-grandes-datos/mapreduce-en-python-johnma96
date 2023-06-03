#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

lista = []
for row in sys.stdin:
  linea = row.strip()
  linea = linea.split(";")
  tupla = (linea[0],linea[1],int(linea[2]))
  lista.append(tupla) 
lista.sort(key=lambda x: (x[0], x[2]))

for tupla in lista:
  line =  tupla[0] + "   " + str(tupla[1]) + "   " + str(tupla[2]) + "\n"
  sys.stdout.write(line) 