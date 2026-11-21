lentoasemat = [{"nimi": "Helsinki-Vantaa", "icao": "EFHK"},
               {"nimi": "Kööpenhaminan lentokenttä", "icao": "EKCH"},
               {"nimi": "Rovaniemen lentoasema", "icao": "EFRO"}]


while True:

    valinta = input("Haluatko syöttää uuden lentoaseman (1), hakea jo syötetyn lentoaseman (2), vai lopettaa (0)?: ")


    if valinta == "0":
        break


    elif valinta == "1":
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        uusi = {"nimi": nimi, "icao": koodi}
        lentoasemat.append(uusi)


    elif valinta == "2":
        koodi = input("Anna ICAO-koodi: ")
        for l in lentoasemat:
            if l["icao"] == koodi:
                print(f"Lentoaseman nimi on {l['nimi']}")
