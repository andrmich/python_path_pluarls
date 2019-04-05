from itertools import islice, count, chain
from math import sqrt


def is_prime(x):
    '''
    Returns True if number is prime else False.
    '''
    if x < 2:
        return False
    # for x in range(2, number):
    #     if number % x == 0:
    #         return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
t = list(thousand_primes)
s = sum(islice((x for x in count() if is_prime(x)), 1000))

is_prime_in_range = any(is_prime(x) for x in range(1328, 1361))

temp_sunday = [12, 15, 16, 20, 7]
temp_monday = [11, 13, 16, 24, 3]

comparison_mn_sun = list(zip(temp_monday, temp_sunday))

average_temp = []
for sun, mon in zip(temp_sunday, temp_monday):
    average_temp.append('Average = {}'.format((sun + mon)/ 2))

temperatures = chain(temp_sunday, temp_monday)
above_zero = all(t>0 for t in temperatures)
if __name__ == '__main__':
    print(t)
    print('sum = ', s)
    print(is_prime_in_range)
    print(comparison_mn_sun)
    print(average_temp)
    print('All temperatures are above zero: ', above_zero)
