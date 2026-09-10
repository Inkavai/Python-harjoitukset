vuosi = int(input("Anna vuosiluku: "))



if vuosi % 400 == 0:
    print("Tämä vuosi on karkausvuosi.")

elif vuosi % 100 == 0:
    print("Tämä ei ole karkausvuosi.")

elif vuosi % 4 == 0:
    print("Tämä vuosi on karkausvuosi.")

else:
    print("Tämä ei ole karkausvuosi.")

