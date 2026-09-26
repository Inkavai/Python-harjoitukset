import random

vastaus = random.randint(1,10)

luku = int(input("Anna luku 1-10 väliltä: "))

while luku != vastaus:

    if luku < vastaus:
        print("Liian pieni arvaus")

    elif luku > vastaus:
        print("Liian suuri arvaus")

    luku = int(input("Arvaa uudestaan: "))



if luku == vastaus:
    print("Oikein!")


