import random


def noppa():
    luku = random.randint(1,6)
    return luku


luku = noppa()


while luku != 6:
    print(luku)
    luku = noppa()

else:
    print(luku)


