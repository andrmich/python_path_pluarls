def sequence(immutable):
    return tuple if True else list


b = sequence(immutable=True)


scientists = ['Marie Curie', 'Albert Einstein', 'Niels Bohr', 'Isaac Newton', 'Dimitri Mendeleev']

c = sorted(scientists, key=lambda name: name.split()[-1])

def is_even(x):
    return x% 2 ==0

d = callable(is_even)



if __name__ == '__main__':
    print(b)
    print(c)
    print(d)
