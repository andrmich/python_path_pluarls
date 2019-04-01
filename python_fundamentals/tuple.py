t = ('Norway', 4.953, 3)

p = 1, 1, 1, 1, 4, 6, 9

print(type(p))


def minmax(items):
    return min(items), max(items)


lower, upper = minmax(p)

(a, (b, (c, d))) = (4, (3, (2, 1)))

e = 'jelly'
f = 'gum'

e, f = f, e

if __name__ == '__main__':
    print(minmax(p))
    print(lower)
    print(a)
    print(e)
