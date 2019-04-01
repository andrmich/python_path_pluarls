s = ['a', 'b', 'c', 'd', 'e']
full_slice = s[:]

if s == full_slice:
    print('Copy made')

if s is full_slice:
    print('Ok')
else:
    print('Not so shallow')

a = [[-1, +1]] * 5

if __name__ == '__main__':
    print(full_slice)
    print(s)
