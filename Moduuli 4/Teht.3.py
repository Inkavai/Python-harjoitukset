vastaus = input("Anna luku: ")

if vastaus != "":
    luku = int(vastaus)
    pieni = luku
    suuri = luku

    while True:
        vastaus = input("Anna luku: ")

        if vastaus == "":
            break

        luku = int(vastaus)

        if luku < pieni:
            pieni = luku

        if luku > suuri:
            suuri = luku

    print("Pienin antamasi luku oli", pieni)
    print("Suurin antamasi luku oli", suuri)