
vastaus = 1

tunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

while vastaus < 5:

    if tunnus == "inka" and salasana == "salasana":
        print("Tervetuloa")
        break
    
    print("Väärä käyttäjä/salasana, yritä uudelleen")

    vastaus = vastaus + 1

    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")


else:
    print("Pääsy evätty.")









