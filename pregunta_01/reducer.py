#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
dict = {}
for row in sys.stdin:
  if row in dict.keys():
    dict[row] += 1
  else:
    dict[row] = 1
for i in dict.keys():
   letra = i.strip()
   line =  letra + "\t" + str(dict[i]) + "\n"
   sys.stdout.write(line)