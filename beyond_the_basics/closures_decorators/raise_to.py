def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


if __name__ == '__main__':
    square = raise_to(2)
    print(square(4))
    cube = raise_to(3)
    print(cube(9))