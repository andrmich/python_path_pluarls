# def hypervolume(*lengths):
#     i = iter(lengths)
#     v = next(i)
#     for length in i:
#         v *= length
#     return v


def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v


# def tag(name, **kwargs):
    # print(name)
    # print(kwargs)
    # print(type(kwargs))


def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result


if __name__ == '__main__':
    print(hypervolume(2, 4, 6))
    print(tag('img', src='monet.jpg', alt='Sunrise', border=1))
