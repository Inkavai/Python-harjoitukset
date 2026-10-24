import math

from math import sqrt

luku = int(input("Anna kokonaisluku: "))

while luku > 0:
    print ("Luvun neliöjuuri on", sqrt(luku))
    luku = int(input("Anna kokonaisluku: "))
   

    if luku < 0:
        print("Virheellinen numero.")
        luku = int(input("Anna kokonaisluku: "))


    elif luku == 0:
        break

