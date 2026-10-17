luku = int(input("Anna kokonaisluku: "))


aluku = True

if luku <= 0:
        aluku = False

for jako in range(2,luku):
    if luku % jako == 0:
        aluku = False

    


if aluku == False:
    print("Luku ei ole alkuluku.")

else:
    print("Luku on alkuluku.")
