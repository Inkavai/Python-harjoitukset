tuotanto = [120, 150, 90, 180, 160]

def analysoi_tuotanto(maara):
    s = 0
    i = 0
    for t in tuotanto:
        s += t
        if t > i:
            i = t
    return float(s), float(i)

yht, isoin = analysoi_tuotanto(tuotanto)

print(tuotanto)

print(f"Tuotanto yhteensä: {yht:.2f} kappaletta.")

print(f"Keskimääräinen päivätuotanto: {yht/5:.2f} kappaletta.")

print(f"Suurin yksittäisen päivän tuotantomäärä: {isoin} kappaletta.")