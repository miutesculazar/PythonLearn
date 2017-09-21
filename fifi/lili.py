def concatenate_list(a, b):
    """
    unite two lists
    :param a: first list
    :param b: second list
    :return:
    """
    a.extend(b)
    return a


if __name__ == "__main__":
    a = [1, 2]
    b = ['a', 3, 'vb']
    print('module: lili -> {}'.format(concatenate_list(a, b)))
