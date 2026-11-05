
lista = [2, 3, 8, 11, 7, 6]


def pari(lista):
    lista1 = []
    for s in lista:
        if s % 2 == 0:
            lista1.append(s)
    return lista1



print(pari(lista))
print(lista)
