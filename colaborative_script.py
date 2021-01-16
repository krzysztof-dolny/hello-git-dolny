tekst = "This is my first Python repository."
print(tekst)
mojaLista = []
for literka in tekst:
    mojaLista.append(literka)
for n in range(len(tekst)):
    print("The ASCII value of '" + mojaLista[n] + "' is", ord(mojaLista[n]))
