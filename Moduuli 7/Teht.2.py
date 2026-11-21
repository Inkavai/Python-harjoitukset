nimet = set()


nimi = input("Anna nimi tai lopeta painamalla Enter: ")


while True:

    if nimi == "":
        break

    elif nimi in nimet:
        print("Aiemmin syötetty nimi.")

    else:
        print("Uusi nimi.")
        nimet.add(nimi)

    nimi = input("Anna nimi tai lopeta painamalla Enter: ")
    


for n in nimet:
    print(n)