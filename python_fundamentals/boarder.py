def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)
    print('\n')


if __name__ == '__main__':
    banner('Norwegian Blue')
    banner('Sun, Moon, Stars', '*')
    banner(border='-', message='Sun, Moon, Stars')
