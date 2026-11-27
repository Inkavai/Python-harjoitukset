def laske_kustannus(hinta, kpl):
    yht = hinta * kpl
    return yht



euro = float(input("Anna tuotteen valmistuskustannus: "))
maara = float(input("Kuinka monta tuotetta valmistetaan?: "))

tulos = laske_kustannus(euro, maara)

print(f"Valmistuksen kokonaisukustannut on {tulos:.2f} €.")