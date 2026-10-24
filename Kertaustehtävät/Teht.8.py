kustannukset = [8.5, 12, 5.3, 4.8, 2]

kaikki = 0

for k in kustannukset:
    print (f"Tuotteen valmistuskustannus: {k}€")
    kaikki += k


print(f"Kustannukset yhteensä: {kaikki}€")