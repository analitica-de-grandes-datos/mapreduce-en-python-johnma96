#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


for row in sys.stdin:
  elementos = row.split(",")
  
  linea = elementos[2]
  linea.replace("\t","")
  sys.stdout.write(linea+"\n")