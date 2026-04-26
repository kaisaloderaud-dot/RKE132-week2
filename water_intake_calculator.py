klaasid = int(input("Mitu klaasi vett oled täna joonud?"))
protsent = (klaasid * 250) /200 * 100

if protsent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif protsent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")
    