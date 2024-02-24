'''
    >>> wyb(19, '3B 4B 5B 4C 5C 3C 1A 5A 5C 3A 5A 2C 1B 2A 5B 5C 2B 1C 4A')
    'TAK'
    >>> wyb(20, '2B 4B 4C 5A 5C 5C 4A 1B 3A 4A 2A 3B 1B 1C 1A 5A 2C 1B 5B 3C')
    'NIE'
    '''


def wyb(n, poz):
    exp_poz = {}
    for i in range(1, 5 + 1):
        for j in ['A', 'B', 'C']:
            exp_poz[f'{i}{j}'] = 2 if i == 5 else 1

    # print(exp_poz)
    for i in poz.split(' '):
        if i in exp_poz and exp_poz[i] > 0:
            exp_poz[i] -= 1
            if sum(exp_poz.values()) == 0:
                return 'TAK'

    # print(exp_poz, sum(exp_poz.values()))
    return 'NIE'


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    # print(wyb(19, '3B 4B 5B 4C 5C 3C 1A 5A 5C 3A 5A 2C 1B 2A 5B 5C 2B 1C 4A'))
    # print(wyb(20, '2B 4B 4C 5A 5C 5C 4A 1B 3A 4A 2A 3B 1B 1C 1A 5A 2C 1B 5B 3C'))
