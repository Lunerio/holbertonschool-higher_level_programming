#!/usr/bin/python3
"""you know what it is"""


lista_big = []
lista_1 = [1]
lista_2 = [1, 1]


def pascal_triangle(n):
    """return list with lists with values of pascal triangle"""
    if n <= 0:
        return lista_big

    if n == 1:
        lista_big.append(lista_1)
        return lista_big

    if n == 2:
        lista_big.append(lista_1)
        lista_big.append(lista_2)
        return lista_big

    lista_big.append(lista_1)
    lista_big.append(lista_2)

    lista_base = lista_2[:]
    new_num = 0
    save_list = []

    for i in range(2, n):
        index = 1

        if (len(lista_base) % 2) == 1:
            limite = int((len(lista_base) + 2) / 2)
            save_list = lista_base[:]

            for j in range(0, limite - 1):
                new_num = lista_base[j] + lista_base[j + 1]
                save_list.insert(index, new_num)
                index += 1

            lista_base = save_list[:]

            for j in range(-1, (limite * -1) - 1, -1):
                lista_base[j] = lista_base[(j * -1) - 1]

        else:
            limite = len(lista_base) - 1
            save_list = lista_base[:]

            for j in range(0, limite):
                new_num = lista_base[j] + lista_base[j + 1]
                save_list.insert(index, new_num)
                index += 1

            lista_base = save_list[:]

            for j in range(-1, (limite * -1), -1):
                lista_base.pop(j - 1)
                lista_base[j] = lista_base[(j * -1) - 1]

        lista_big.append(lista_base)


    return lista_big
