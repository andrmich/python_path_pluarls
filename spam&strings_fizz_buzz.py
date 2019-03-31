def divide_3(number):
    if number % 3 == 0:
        return True
    else:
        return False


def divide_5(number):
    if number % 5 == 0:
        return True
    else:
        return False


def fizz_buzz(number: int) -> str:
    if divide_3(number) and divide_5(number) is True:
        return 'Fizz Buzz'
    elif divide_3(number) is True and divide_5(number) is False:
        return 'Fizz'
    elif divide_3(number) is False and divide_5(number) is True:
        return 'Buzz'
    else:
        return str(number)


if __name__ == '__main__':
    print(fizz_buzz(15))
    assert fizz_buzz(6) == "Fizz", "6 is divisible by 3"
    assert fizz_buzz(5) == "Buzz", "5 is divisible by 5"
    assert fizz_buzz(7) == "7", "7 is not divisible by 3 or 5"
