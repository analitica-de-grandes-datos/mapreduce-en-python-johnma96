#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
from datetime import date

def prettyformat(x):
  if x <10:
    x = "0"+str(x)
  else:
    x =  str(x)
  return x

for row in sys.stdin:
  elementos = row.strip()
  elementos = elementos.split("   ")
  
  valor = date.fromisoformat(elementos[1])
  mes = prettyformat(valor.month)

   
  sys.stdout.write(mes+"\n")