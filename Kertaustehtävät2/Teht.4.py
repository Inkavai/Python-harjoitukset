hedelmat = {"omena": 0.5, "päärynä": 0.3, "banaani": 0.1, "luumu": 0.4}

hedelma = input("Minkä hedelmän hinnan haluat tietää? (Lopeta painamalla Enter): ")

yht = 0

while True:

    if hedelma == "":
            break

    elif hedelma in hedelmat:
        print(f"{hedelma} maksaa {hedelmat[hedelma]} €.")
        yht += float(hedelmat[hedelma])
        hedelma = input("Minkä hedelmän hinnan haluat tietää? (Lopeta painamalla Enter): ")


    elif hedelma not in hedelmat:
        print("Hedelmä ei löydy hinnastosta.")
        vastaus = input("Haluatko lisätä hedelmän hinnastoon? (K = Kyllä, E = Ei):").upper()
        if vastaus == "K":
                hinta = float(input("Anna tuotteen hinta: "))
                hedelmat[hedelma] = hinta

        

print(f"Yhteensä hinta on {yht:.2f}€.")
print(hedelmat)
