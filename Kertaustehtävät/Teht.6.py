lista = []


arvo = int(input("Syötä arvo tai lopeta painamalla 0: "))

while arvo != 0:
    lista.append(int(arvo))

    arvo = int(input("Anna uusi arvo tai lopeta painamalla 0: "))


print(lista)

lista.sort(reverse=False)
print(lista)



