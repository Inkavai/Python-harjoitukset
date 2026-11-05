import random


def noppa(maksimi):
    luku = random.randint(1, maksimi)
    return luku

maksimi = int(input("Anna nopalle maksimisilmäluku: "))

luku = noppa(maksimi)


while luku != maksimi:
    print(luku)
    luku = noppa(maksimi)

else:
    print(luku)

