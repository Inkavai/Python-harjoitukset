sana = input("Anna sana lisättäväksi tarinaan: ")

tarina = " "


while sana != "loppu":
    tarina = tarina + " " + sana
    sana = input("Anna sana lisättäväksi tarinaan: ")


else:
    print(tarina)