from math import factorial


# How many different groups of k elements of fruit we can pick
# from n different fruits
def no_of_combinations(fruits: int, gr_count):
    return factorial(fruits) // (factorial(gr_count) * factorial(fruits - gr_count))


if __name__ == '__main__':
    print(no_of_combinations(100, 2))
