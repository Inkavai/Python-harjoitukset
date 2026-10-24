lista = ["inka", "sadekeli", "koira", "lelu", "ruoka", "lohikeitto"]


sanat = 0

for s in lista:
    if len(s) >5:
        sanat += 1


print ("Yli 5 kirjainta sisältäviä sanoja yhteensä", sanat, "kappaletta.")