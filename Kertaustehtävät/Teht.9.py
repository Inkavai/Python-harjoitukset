tuotanto = []
maarat = []

tuote = input("Mitä tuotetta valmistetaan?: ")
monta = int(input("Kuinka monta valmistetaan?: "))
vastaus = input("Jatketaanko tuotantoa (kyllä/ei)?: ").lower()

tuotanto.append(tuote)
maarat.append(monta)

while True:
    if vastaus == "kyllä":
  
        tuote = input("Mitä tuotetta valmistetaan?: ")
        monta = int(input("Kuinka monta valmistetaan?: "))
        vastaus = input("Jatketaanko tuotantoa (kyllä/ei)?: ").lower()

        tuotanto.append(tuote)
        maarat.append(monta)

    
    elif vastaus == "ei":
           break

    
for t in range(len(tuotanto)):
            print(f"Tuote: {tuotanto[t]}, määrä: {maarat[t]}")