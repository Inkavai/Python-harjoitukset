palkka = float(input("Anna tuntipalkka: "))

tehty = float(input("Montako tuntia tehty töitä? "))

paiva = input("Minä viikonpäivänä työ on tehty?: ").lower()


raha = palkka * tehty

if paiva == "sunnuntai":
    raha *= 2
    print("Sait päivän aikana palkkaa", raha, "euroa, tuplaliksa on jees!")

elif paiva in ["maanantai", "tiistai", "keskiviikko", "torstai", "perjantai","lauantai"]:
    print ("Sait päivän aikana palkkaa", raha, "euroa.")


else:
    print("Virheellinen viikonpäivä.")




