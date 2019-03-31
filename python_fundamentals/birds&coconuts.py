from math import ceil


def no_of_swallows_to_carry(weight: float):
    swallow_limit = 60 / 3
    return ceil(weight / swallow_limit)


if __name__ == '__main__':
    print(no_of_swallows_to_carry(8))
    coconut = 1450
    print(no_of_swallows_to_carry(coconut))
