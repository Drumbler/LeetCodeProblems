import string


def my_func():
    n = int(input('Число кандидатов: '))
    candidates = []
    for _ in range(n):
        f, i, o, d, m, y = input(
            'Введите данные кандидата (Фамилия, Имя, Отчество, День, Месяц, Год): ').split(',')
        candidates.append({'f': f, 'i': i, 'o': o,
                          'd': int(d), 'm': int(m), 'y': int(y)})
    res: list = []
    for i in candidates:
        res.append([len(set(i['f'] + i['i'] + i['o'])),
                   (i['d'] % 10 + i['d'] // 10 + i['m'] %
                    10 + i['m'] // 10) * 64,
                    (string.ascii_uppercase.index(i['f'][0]) + 1) * 256 if i['f'][0] in string.ascii_uppercase else (
                        string.ascii_lowercase.index(i['f'][0]) + 1) * 256,
                    ])

    return ' '.join([hex(sum(i))[-3:].upper() for i in res])

    # res[candidate_N].append(len(
    #     set(i['f'] + i['i'] + i['o'])) + 1)
    # res.append((i['d'] % 10 + i['d'] //
    #            10 + i['m'] % 10 + i['m'] // 10) * 64)
    # if i['f'][0] in string.ascii_uppercase:
    #     res[candidate_N].append((string.ascii_uppercase.index(
    #         i['f'][0]) + 1) * 256)
    # elif i['f'][0] in string.ascii_lowercase:
    #     res[candidate_N].append((string.ascii_lowercase.index(
    #         i['f'][0]) + 1) * 256)
    #     candidate_N += 1
    # fio_len = len(
    #     set(candidates[0]['f'] + candidates[0]['i'] + candidates[0]['o'])) + 1
    # if candidates[0]['f'][0] in string.ascii_uppercase:
    #     f_first_letter = string.ascii_uppercase.index(
    #         candidates[0]['f'][0]) + 1
    # elif candidates[0]['f'][0] in string.ascii_lowercase:
    #     f_first_letter = string.ascii_lowercase.index(
    #         candidates[0]['f'][0]) + 1

    # print(fio_len)
    # print(f_first_letter)
    # print(candidates[0]['f'][0])


print(my_func())
