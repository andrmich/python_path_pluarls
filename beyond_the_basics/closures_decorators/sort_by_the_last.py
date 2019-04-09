import random
import string


def random_string(stringLength=10):
    '''Generates a random string fo a fixed length.'''
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def string_list(number_of_strings, stringLength):
    '''Generates a list of n random strings.'''
    return [random_string(stringLength) for _ in range(number_of_strings)]


def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)


if __name__ == '__main__':
    print(sort_by_last_letter(string_list(14, 4)))
