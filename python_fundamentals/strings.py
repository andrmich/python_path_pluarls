import math

k = 'unforgetable'.partition('forget')
departure, separator, arrival = 'London:Edinburgh'.partition(':')

departure1, _, arrival1 = '1London:1Edinburgh'.partition(':')

m = 'The age of {0} is {1}'.format ('Jim', 32)

pos = (65, 21, 82)

n = 'Galactic position x={pos[0]} y={pos[1]} z={pos[2]}'.format(pos=pos)

p = 'Math constans: pi = {m.pi}'.format(m=math)
e = 'Math constans: e = {m.e:.3f}'.format(m=math)

if __name__ == '__main__':
    print(k)
    print(arrival)
    print(departure1)
    print(m)
    print(n)
    print(p)
    print(e)
