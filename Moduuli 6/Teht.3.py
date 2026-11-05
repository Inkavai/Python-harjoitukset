gallona = float(input("Anna gallonamäärä (negatiivinen luku lopettaa: )"))

def maara(gallona):
    litra = gallona * 3.785
    return litra


while gallona >= 0:
    litra = maara(gallona)
    print("Määrä on ",litra, "litraa.")
    gallona = float(input("Anna gallonamäärä (negatiivinen luku lopettaa: )"))