#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
  elementos = row.strip()
  elementos = elementos.split("\t")
  
  letra = elementos[0]
  valor = elementos[-1]
  
  sys.stdout.write(letra + ";" + valor + "\n")