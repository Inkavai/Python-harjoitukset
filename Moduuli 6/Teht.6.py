import math

halkaisija1 = float(input("Anna pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna pizzan hinta: "))


halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna pizzan hinta: "))


def pizza(koko, euro):
    sade = koko / 2
    ala = (sade / 100) **2 * math.pi
    hinta = euro / ala
    return hinta


pizza1 = pizza(halkaisija1, hinta1)

pizza2 = pizza(halkaisija2, hinta2)


if pizza1 < pizza2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")

elif pizza1 > pizza2:
    print("Toinen pizza antaa paremman vastineen rahalle.")

else:
    print("Pizzat ovat samanarvoisia.")


print(f"Pizzojen yksikköhinnat ovat {pizza1:.2f} ja {pizza2:.2f} euroa.")

    