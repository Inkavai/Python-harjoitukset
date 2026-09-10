sukupuoli = input("Kerro biologinen sukupuolesi: ")

arvo = int(input("Kerro hemoglobiiniarvosi "))

if sukupuoli == "Nainen":
    if arvo >= 117 and arvo <= 175:
        print ("Hemoglobiiniarvosi on normaali.")

    elif arvo <117:
        print ("Hemoglobiiniarvosi on alhainen.")

    elif arvo >175:
        print("Hemoglobiiniarvosi on korkea.")


if sukupuoli == "Mies":
    if arvo >= 134 and arvo <= 195:
        print("Hemoglobiiniarvosi on normaali.")

    elif arvo <134:
        print("Hemoglobiiniarvosi on alhainen.")

    elif arvo > 195:
        print("Hemoglobiiniarvosi on korkea.")


