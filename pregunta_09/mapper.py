#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for row in sys.stdin:
  elementos = row.strip()
  elementos = elementos.split("   ")
  
  letra = elementos[0]
  valor = elementos[2]
  fecha = elementos[1]
  sys.stdout.write(letra + ";" + fecha + ";" + valor + "\n")