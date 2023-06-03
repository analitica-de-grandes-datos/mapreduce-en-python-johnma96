#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
for row in sys.stdin:
  elementos = row.strip()
  elementos = elementos.split(",")
  
  cantidad = elementos[1]
  letra = elementos[0]
  linea = letra + ";" + cantidad
  sys.stdout.write(linea+"\n")