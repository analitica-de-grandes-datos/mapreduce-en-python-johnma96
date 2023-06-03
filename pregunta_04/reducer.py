#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys       
if __name__ == '__main__':
    l = []  
    for line in sys.stdin:
        line = line.strip().split()
        l.append(line)
    for i in sorted(set([i[0] for i in l]),key=lambda x: x[0]):
        sys.stdout.write('{},{}\n'.format(i,l.count([i])))