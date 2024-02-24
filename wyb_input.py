def wyb():
    n = list(map(int, input().split()))
    poz = list(map(str, input().split()))
    # print(n, poz)

    exp_poz = {}
    for i in range(1, 5 + 1):
        for j in ['A', 'B', 'C']:
            exp_poz[f'{i}{j}'] = 2 if i == 5 else 1

    # print(exp_poz)
    # for i in poz.split(' '):
    for i in poz[0:n[0]]:
        if i in exp_poz and exp_poz[i] > 0:
            exp_poz[i] -= 1
            if sum(exp_poz.values()) == 0:
                return 'TAK'

    # print(exp_poz, sum(exp_poz.values()))
    return 'NIE'


if __name__ == '__main__':
    print(wyb())
