kurssitiedot = {"Matti": ["Biologia", "Kemia", "Matematiikka"], "Heidi": ["Liikunta", "Matematiikka"], "Juhani": ["Kemia", "Liikunta", "Äidinkieli"]}


print("Kaikkien oppilaiden kurssitiedot:")
for nimi in kurssitiedot:
    print(f"{nimi} - {kurssitiedot[nimi]}")


uusi = input("Anna uuden oppilaan nimi: ")
kurssitiedot[uusi] = []
while True:
    kurssi = input(f"Lisää oppilaalle {uusi} kurssi tietojärjestelmään tai lopeta painamalla Enter: ")


    
    if kurssi == "":
        break


    kurssitiedot[uusi].append(kurssi)



print("Kaikkien oppilaiden kurssitiedot:")
for nimi in kurssitiedot:
    print(f"{nimi} - {kurssitiedot[nimi]}")




def arvo():
    kurssi = input("Minkä kurssin opiskelijamäärän haluat tietää?: ")

    maara = 0
    for nimi in kurssitiedot:
        if kurssi in kurssitiedot[nimi]:
            maara += 1

    print(f"Kurssilla {kurssi} on {maara} opiskelijaa.")
    return


arvo()
    

