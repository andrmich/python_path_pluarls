names_and_ages = [('Alice', 32), ('Tom', 14), ('Jane', 92)]

d = dict(names_and_ages)

# copy

e = d.copy()
f = dict(d)

g = {'indigo': 1, 'blue': 2}
h = f.update(g)

for key, value in f.items():
    print('{key} => {value}'.format(key=key, value=value))

if __name__ == '__main__':
    print(d)
    print(e)
    print(f)
    print(h)
