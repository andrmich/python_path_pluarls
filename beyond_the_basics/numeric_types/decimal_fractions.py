from decimal import Decimal
from fractions import Fraction

two_thirds = Fraction(2, 3)
one_tenth_un = Fraction(0.1)
one_tenth = Fraction(Decimal('0.1'))

sample = Fraction('22/7')

base_conversions = int('2a', base=16)
base_conversions_1 = int('acghd', base=18)

if __name__ == '__main__':
    print(two_thirds)
    print(one_tenth_un)
    print(one_tenth)
    print(sample)
    print(base_conversions)
    print(base_conversions_1)
