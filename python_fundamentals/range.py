for i in range(5):
    print(i)
# first argument is optional; not normally possible

b = list(range(0, 78, 3))
print('\n')

s = [0, 1, 4, 6, 13]
for v in s:
    print(v)

for z in enumerate(s):
    print(z)

for i, k in enumerate(s):
    print('i = {}, k = {}'.format(i, k))

print('\n')
if __name__ == '__main__':
    print(b)
