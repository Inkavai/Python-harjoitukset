import random


arpa = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

for a in range(arpa):
    summa += random.randint(1,6)

print("Silmälukujen summa on", summa)

