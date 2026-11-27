def laske_voitto(maksu, myynti, kpl):
    h = myynti * kpl - maksu * kpl
    return h



kustannus = float(input("Anna tuotteen valmistuskustannus: "))
hinta = float(input("Anna tuotteen myyntihinta: "))
maara = float(input("Kuinka monta tuotetta myytiin?: "))


tulos = laske_voitto(kustannus, hinta, maara)

print(f"Kokonaisvoitto: {tulos:.2f}€")


if tulos > 0:
    print("Tuotanto on kannattavaa!")


else:
    print("Tuotanto on tappiollista!")