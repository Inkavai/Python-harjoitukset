

leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))


luoditg = luodit*13.3

naulatg = naulat * 32 * 13.3

leiviskätg = leiviskät * 20 * 32 * 13.3

yhteissumma = luoditg + naulatg + leiviskätg


kilot = int(yhteissumma // 1000)

grammat = int(yhteissumma % 1000)

print("Massa on nykymittojen mukaan",kilot,"kilogrammaa ja",grammat,"grammaa.")



