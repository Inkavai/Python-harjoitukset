varasto = {"Pöytä": 20, "Tuoli": 50, "Hylly": 15}

print("Varastotilanne:")
for tuote in varasto:
    print(f"{tuote}: {varasto[tuote]} kpl")


tuote = input("Mitä tuotetta lisätään varastoon?: ")
maara = int(input("Kuinka monta lisätään?: "))

if tuote in varasto:
    varasto[tuote] += maara

elif tuote not in varasto:
    varasto[tuote] = maara            


print("Varastotilanne:")
for tuote in varasto:
    print(f"{tuote}: {varasto[tuote]} kpl")