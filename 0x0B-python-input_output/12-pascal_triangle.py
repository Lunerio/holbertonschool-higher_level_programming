#!/usr/bin/python3
"""you know what it is"""


lista_big = []
lista_1 = [1]
lista_2 = [1, 1]
new_number = 0


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

    prev_list = lista_2[:]

    for i in range(2, n):
        new_list = []
        limit = len(prev_list) - 1

        for i in range(0, limit):
            new_number = prev_list[i] + prev_list[i + 1]
            new_list.append(new_number)

        new_list.insert(0, 1)
        new_list.insert(limit + 1, 1)
        lista_big.append(new_list)
        prev_list = new_list[:]

    return lista_big
